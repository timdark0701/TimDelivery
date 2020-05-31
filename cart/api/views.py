from rest_framework import viewsets
from ..cart import Cart
from rest_framework.response import Response
from main.api import serializers as main_serializers
from django.shortcuts import get_object_or_404, redirect
from main import models as main_models
from . import serializers


class CartView(viewsets.ViewSet):
    def details(self, request):
        cart = Cart(request)
        data = {'items': [item for item in cart]}
        data.update({'total_cost': cart.get_total_cost()})
        for i in range(len(data['items'])):
            data['items'][i]['product'] = main_serializers.FoodSerializer(data['items'][i]['product'],
                                                                          context={'request': request}).data['url']
        return Response(data)

    def add(self, request, food_slug):
        cart = Cart(request)
        food = get_object_or_404(main_models.Food, slug=food_slug)
        cart.add(food, quantity=1, update_quantity=False)
        return Response({
            'cart_quantity': cart.__len__(),
            'cart_total': cart.get_total_cost()
        })

    def update(self, request, food_slug):
        cart = Cart(request)
        food = get_object_or_404(main_models.Food, slug=food_slug)
        quantity = request.data['quantity']
        updatable = request.data['update']

        if type(int(quantity)) == int and 1 <= int(quantity) <= 10:
            if updatable == 'True' or updatable == 'False':
                cart.add(food, quantity=int(quantity), update_quantity=updatable)
                return redirect('cart_details_api')
            else:
                return redirect('cart_update_api', food_slug)
        else:
            return redirect('cart_update_api', food_slug)

    def remove(self, request, food_slug):
        cart = Cart(request)
        food = get_object_or_404(main_models.Food, slug=food_slug)
        cart.remove(food)
        if cart:
            return redirect('cart_details_api')
        return redirect('homepage_api')
