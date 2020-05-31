from django.shortcuts import render, redirect, get_object_or_404
from . import models
from cart import forms as cart_forms


# Create your views here.
# TODO some views


def homepage(request):
    context = dict()

    # List of all restaurant types
    all_types = models.RestaurantType.objects.all()
    context['all_types'] = all_types

    if request.session.has_key('city_id'):
        current_city = models.City.objects.get(id=request.session['city_id'])
        context['all_types'] = all_types.filter(city=current_city)

    return render(request, 'main/homepage.html', context)


def set_city(request, city_id):
    request.session['city_id'] = city_id
    return redirect('main:homepage')


def restaurant_details(request, rest_slug):
    restaurant = get_object_or_404(models.Restaurant, slug=rest_slug)
    context = {'rest': restaurant}
    foods = restaurant.foods.all()
    all_food_types = set([food.food_type for food in foods])
    context['all_food_types'] = all_food_types
    all_foods = dict()
    for food_type in all_food_types:
        all_foods[food_type] = []
        for food in foods:
            if food in food_type.foods.all():
                all_foods[food_type].append(food)

    context['all_foods'] = all_foods

    return render(request, 'main/restaurant_details.html', context)


def search(request):
    context = {'all_rests': []}
    if 'search' in request.GET:
        query = request.GET['search']
        rests = models.Restaurant.objects.all()
        for rest in rests:
            if query.lower() in rest.name.lower():
                context['all_rests'].append(rest)
    return render(request, 'main/search.html', context)


def food_details(request, food_slug):
    food = models.Food.objects.get(slug=food_slug)
    context = {'food': food}
    cart_form = cart_forms.CartAddProductForm()
    context['cart_form'] = cart_form
    return render(request, 'main/food_details.html', context)


