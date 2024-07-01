from django.urls import path
from . import views

urlpatterns = [
    path('pessoa/', views.getData),
    path('pessoa/add/', views.addData),
    path('pessoa/<int:pk>/update/', views.updateData),  
    path('pessoa/<int:pk>/delete/', views.deleteData),
    path('pessoa/login/', views.login),
]