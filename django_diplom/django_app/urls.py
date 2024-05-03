from django.urls import path, re_path
from django_app import views

urlpatterns = [
    path('', views.Home.as_view(), name=''),
    path('index/', views.Home.as_view(), name='index'),
    path('home/', views.Home.as_view(), name='home'),
    re_path(r"^home/", views.Home.as_view(), name='home'),
    re_path(r"^contact/(?P<contact_id>\d+)/delete/$", views.contact_delete, name="contact_delete"),
    path('index_http/', views.index_http, name='index_http'),
    path('index_json/', views.index_json, name='index_json'),
]
