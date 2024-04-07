"""
URL configuration for django_settings project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django_app import views

urlpatterns = [
    path('', views.index),
    path('api/', views.api),
    path('api/persons/', views.get_persons),
    path('api/persons/<str:tabel_num>/', views.get_person),
    path('api/categories/', views.get_categories),
    path('api/categories/<int:id>/', views.get_category),
    path('api/clothes/', views.get_clothes),
    path('api/clothes/<int:id>/', views.get_clothes),
               ]
