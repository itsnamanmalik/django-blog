from django.urls import path, re_path, include
from api import views


# /MadLearners/

urlpatterns = [
    # re_path(r'^$', views.index, name='MadLearners'),
    path('blogapi/',views.blogAPI),
    path('categoryapi/',views.categoryAPI),
    path('videoapi/',views.videoAPI),

    # path('login/', views.LoginView.as_view()),
    # path('logout/', views.LogoutView.as_view()),



    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.authtoken')),
    # path('register/', views.registration_view, name="register"),
]
