from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .cart import Cart
from main import models
from django.views.decorators.http import require_POST
from django.http import JsonResponse
# Create your views here.


def cart_add(request):
    cart = Cart(request)
    food = get_object_or_404(models.Food, slug=request.GET['food_slug'])
    cart.add(food, quantity=1, update_quantity=False)
    return JsonResponse({
        'cart_quantity': cart.__len__(),
        'cart_total': cart.get_total_cost()
    })


@require_POST
def cart_update(request, food_slug):
    cart = Cart(request)
    food = get_object_or_404(models.Food, slug=food_slug)
    form = forms.CartAddProductForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(food, quantity=cd['quantity'], update_quantity=cd['update'])
        return redirect('cart:cart_detail')
    else:
        return redirect('main:food_details', food_slug)


def cart_remove(request, food_slug):
    cart = Cart(request)
    food = get_object_or_404(models.Food, slug=food_slug)
    cart.remove(food)
    if cart:
        return redirect('cart:cart_detail')
    return redirect('main:homepage')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = forms.CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/detail.html', {'cart': cart, 'len': cart.cart.__len__()})


