from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.register,name='register'),
    path('login', views.login,name='login'),
    path('map', views.map,name='map'),
]