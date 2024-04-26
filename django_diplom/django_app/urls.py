from django.contrib import admin
from django.urls import path

from django_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('home/', views.index, name='index'),
]
