from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Post


# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': "Home page",
    }
    return render(request, template_name="blog/home.html", context=context)


def about(request):
    return render(request, template_name="blog/about.html", context={'title': "About page"})


def all_users(request):
    context = {
        'users': User.objects.all(),
        'title': 'All Users'
    }
    return render(request, template_name="blog/all_users.html", context=context)
