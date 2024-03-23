from django.urls import path
from django_app import views

urlpatterns = [
    path('api/', views.api),
    path('api/contracts/', views.contract_list),
    path("api/comments/", views.get_comment),
    path("api/agents/", views.get_agent),
    path('api/contracts/<int:pk>/', views.contract_detail),
    path('api/contracts/create/', views.contract_create),
    path('api/contracts/<int:pk>/update/', views.contract_update),
    path('api/contracts/<int:pk>/delete/', views.contract_delete),
    path("api/get_contract_by_author/<int:pk>", views.get_contract_by_author)

]
