from django.urls import path, re_path, include
from accounts import views


urlpatterns = [
    path('register/',views.user_register,name='user_register'),
    path('login/',views.user_login,name='user_login'),
    path('logout/', views.user_logout, name='logoutuser'),
    path('profile/', views.profile, name='profile'),
]
