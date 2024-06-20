from django.urls import path
from . import views

urlpatterns = [
    path('update/<int:pk>/', views.update_profile, name='update_profile'),
    path('delete/<int:pk>/', views.delete_profile, name='delete_profile'),
]
