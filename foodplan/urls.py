from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_food_plan, name='add_food_plan'),
    path('update/<int:pk>/', views.update_food_plan, name='update_food_plan'),
    path('', views.foodplan_list, name='foodplan_list'),
]
