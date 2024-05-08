from django.urls import path
from django_app import views

app_name = "django_app"

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
]
