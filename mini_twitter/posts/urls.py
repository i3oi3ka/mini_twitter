from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.posts_list, name='posts_list'),
    path('comments/', views.comments_list, name='comments_list'),
]