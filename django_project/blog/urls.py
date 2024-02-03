from django.urls import path
from . import views

# urls for {% url 'blog-home' %}
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('all_users/', views.all_users, name='blog-all_users')
]
