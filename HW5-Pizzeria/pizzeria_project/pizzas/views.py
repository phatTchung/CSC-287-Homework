from django.shortcuts import render, get_object_or_404
from .models import Pizza

def home(request):
    return render(request, 'pizzas/home.html')

def pizza_list(request):
    pizzas = Pizza.objects.all().order_by('name')
    return render(request, 'pizzas/pizza_list.html', {'pizzas': pizzas})

def pizza_detail(request, pizza_id):
    pizza = get_object_or_404(Pizza, id=pizza_id)
    toppings = pizza.topping_set.all().order_by('name')
    return render(request, 'pizzas/pizza_detail.html', {'pizza': pizza, 'toppings': toppings})
