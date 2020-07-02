from django.urls import path, re_path, include
from blog import views


urlpatterns = [
    path('', views.blog, name='blog'),
    path('<str:slug>/', views.blogPost, name='blogPost'),
]
