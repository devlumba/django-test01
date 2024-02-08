from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView)
from .models import Post, ImagePost, VideoPost


# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': "Home page",
    }
    return render(request, template_name="blog/home.html", context=context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'   # <app>/<model>_<viewtype>.html    # blog/post_list.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 24


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"
    template_name = 'blog/post/post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class ImagePostListView(ListView):
    model = ImagePost
    template_name = 'blog/image_post/home-images.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 40


class ImagePostDetailView(DetailView):
    model = ImagePost
    template_name = 'blog/image_post/imagepost_detail.html'


class ImagePostCreateView(LoginRequiredMixin, CreateView):
    model = ImagePost
    fields = ['title', 'content']
    template_name = 'blog/image_post/imagepost_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ImagePostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ImagePost
    fields = ['title', 'content']
    template_name = 'blog/image_post/imagepost_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class ImagePostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ImagePost
    success_url = "images_posts/"
    template_name = 'blog/image_post/imagepost_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class VideoPostListView(ListView):
    model = VideoPost
    template_name = 'blog/video_post/home-videos.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 40


class VideoPostDetailView(DetailView):
    model = VideoPost
    template_name = 'blog/video_post/videopost_detail.html'


class VideoPostCreateView(LoginRequiredMixin, CreateView):
    model = VideoPost
    fields = ['title', 'content']
    template_name = 'blog/video_post/videopost_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class VideoPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = VideoPost
    fields = ['title', 'content']
    template_name = 'blog/video_post/videopost_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class VideoPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = VideoPost
    success_url = "/"
    template_name = 'blog/video_post/videopost_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class UserDetailView(DetailView):
    model = User
    template_name = 'blog/user/user_detail.html'
    context_object_name = 'some_user'


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user/user_posts.html'   # <app>/<model>_<viewtype>.html    # blog/post_list.html
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    success_url = "/"
    template_name = "blog/user/user_confirm_delete.html"

    def test_func(self):
        user = self.get_object()
        if self.request.user == user:
            return True
        else:
            return False


class UserListView(ListView):
    model = User
    template_name = "blog/user/user_list.html"
    context_object_name = 'users'
    ordering = ['date_joined']
    paginate_by = 10


def about(request):
    return render(request, template_name="blog/about.html", context={'title': "About page"})


def create_post(request):
    return render(request, template_name="blog/create.html", context={"title": "Create Post"})

# not used anymore
#
# def all_users(request):
#     context = {
#         'users': User.objects.all(),
#         'title': 'All Users'
#     }
#     return render(request, template_name="blog/all_users.html", context=context)
