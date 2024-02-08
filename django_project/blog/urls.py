from django.urls import path
from .views import (PostListView, PostDetailView, UserDetailView, PostCreateView, PostUpdateView, PostDeleteView,
                    ImagePostDetailView, ImagePostListView, ImagePostCreateView, ImagePostDeleteView,
                    ImagePostUpdateView,
                    VideoPostListView, VideoPostDeleteView, VideoPostCreateView, VideoPostDetailView,
                    VideoPostUpdateView,
                    UserPostListView, UserDeleteView, UserListView)
from . import views

# urls for {% url 'blog-home' %}
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('create/', views.create_post, name='create'),
    path('about/', views.about, name='blog-about'),
    path('all_users/', UserListView.as_view(), name='blog-all_users'),
    path('user/posts/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('user/<int:pk>/delete', UserDeleteView.as_view(), name='user-delete'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('image_posts/', ImagePostListView.as_view(), name='blog-home_images'),
    path('image_posts/<int:pk>/', ImagePostDetailView.as_view(), name='image_post-detail'),
    path('image_posts/new/', ImagePostCreateView.as_view(), name='image_post-create'),
    path('image_posts/<int:pk>/update', ImagePostUpdateView.as_view(), name='image_post-update'),
    path('image_posts/<int:pk>/delete', ImagePostDeleteView.as_view(), name='image_post-delete'),
    path('video_posts/', VideoPostListView.as_view(), name='blog-home_videos'),
    path('video_posts/<int:pk>/', VideoPostDetailView.as_view(), name='video_post-detail'),
    path('video_posts/new/', VideoPostCreateView.as_view(), name='video_post-create'),
    path('video_posts/<int:pk>/update', VideoPostUpdateView.as_view(), name='video_post-update'),
    path('video_posts/<int:pk>/delete', VideoPostDeleteView.as_view(), name='video_post-delete'),
]
