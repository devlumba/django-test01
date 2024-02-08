import os
from uuid import uuid4

from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.deconstruct import deconstructible
from PIL import Image


@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.path, filename)


path_and_rename = PathAndRename("profile_pics")


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey(User, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class ImagePost(models.Model):
    title = models.CharField(max_length=100)
    content = models.ImageField(upload_to=path_and_rename)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.content.path)

        if img.height > 1000 or img.width > 1000:
            output_size = (1000, 1000)
            img.thumbnail(output_size)
            img.save(self.content.path)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('image_post-detail', kwargs={'pk': self.pk})


class VideoPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.FileField(upload_to=path_and_rename, null=True, validators=[FileExtensionValidator(
                                 allowed_extensions=['mp4'])])
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('video_post-detail', kwargs={'pk': self.pk})
