from django.urls import path, re_path, include
from home import views


# /MadLearners/

urlpatterns = [
    # re_path(r'^$', views.index, name='MadLearners'),

    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('app-privacy-policy/', views.privacy_policy, name='privacy_poliocy'),
] 