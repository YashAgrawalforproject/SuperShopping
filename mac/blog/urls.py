from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('postComment', views.postComment, name="postComment"),
    path('search', views.search, name="search"),
    path('', views.blogHome, name="bloghome"),
    path('<str:slug>', views.blogPost, name="blogPost"),
]
