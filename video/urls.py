from django.urls import path, re_path, include
from video import views


# /MadLearners/

urlpatterns = [
    # re_path(r'^$', views.index, name='MadLearners'),

    path('', views.videos, name='videos'),
    path('<str:slug>', views.single_video, name='single_video'),
] 