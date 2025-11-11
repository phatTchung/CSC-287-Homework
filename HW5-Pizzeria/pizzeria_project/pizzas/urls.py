from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pizzas/', views.pizza_list, name='pizza_list'),
    path('pizzas/<int:pizza_id>/', views.pizza_detail, name='pizza_detail'),
]
