# HW5 - Pizzeria

## How to run
1. Create and activate a virtual environment.
2. `cd pizzeria_project`
3. `python manage.py migrate`
4. `python manage.py createsuperuser` (optional to add data)
5. `python manage.py runserver`
6. Visit `http://127.0.0.1:8000/` (Home), `http://127.0.0.1:8000/pizzas/` (List), click a pizza (Detail).

## What’s included
- App `pizzas` with models `Pizza` and `Topping` 
- Admin registration for both models
- Template inheritance: `base.html` → `home.html`, `pizza_list.html`, `pizza_detail.html`
- URLs wired in `pizzeria_project/urls.py` and `pizzas/urls.py`
