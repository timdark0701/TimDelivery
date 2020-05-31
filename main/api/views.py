from rest_framework import viewsets
from rest_framework.response import Response
from . import serializers
from .. import models
from ..context_processor_api import common_context
from django.shortcuts import get_object_or_404, redirect

# Model Viewsets


class CityView(viewsets.ModelViewSet):
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer


class FoodTypeVIew(viewsets.ModelViewSet):
    queryset = models.FoodType.objects.all()
    serializer_class = serializers.FoodTypeSerializer


class RestaurantTypeView(viewsets.ModelViewSet):
    queryset = models.RestaurantType.objects.all()
    serializer_class = serializers.RestaurantTypeSerializer


class RestaurantView(viewsets.ModelViewSet):
    queryset = models.Restaurant.objects.all()
    serializer_class = serializers.RestaurantSerializer


class IngredientView(viewsets.ModelViewSet):
    queryset = models.Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer


class FoodView(viewsets.ModelViewSet):
    queryset = models.Food.objects.all()
    serializer_class = serializers.FoodSerializer


class MainView(viewsets.ViewSet):
    food_ser = serializers.FoodSerializer
    f_type_ser = serializers.FoodTypeSerializer
    rest_ser = serializers.RestaurantSerializer
    r_type_ser = serializers.RestaurantTypeSerializer
    ing_ser = serializers.IngredientSerializer
    city_ser = serializers.CitySerializer

    def context(self, request):
        return {'request': request}

    def homepage(self, request):
        all_types = models.RestaurantType.objects.all().order_by('id')
        if request.session.has_key('city_id'):
            current_city = models.City.objects.get(id=request.session['city_id'])
            all_types = all_types.filter(city=current_city)
        data = {'all_types': self.r_type_ser(all_types, many=True, context=self.context(request)).data}

        data.update(common_context(request))
        return Response(data)

    def set_city(self, request, city_id):
        request.session['city_id'] = city_id
        # return Response({'city_id': request.session['city_id']})
        return redirect('homepage_api')

    def restaurant_details(self, request, rest_slug):
        restaurant = get_object_or_404(models.Restaurant, slug=rest_slug)
        data = {'restaurant': self.rest_ser(restaurant, context=self.context(request)).data}    # Restaurant Serializer
        foods = restaurant.foods.all()
        all_food_types = sorted(list(set([food.food_type for food in foods])))
        data['food_types'] = dict()
        for food_type in all_food_types:
            food_type_url = self.f_type_ser(food_type, context=self.context(request)).data['url']
            data['food_types'][food_type_url] = []
            for food in foods:
                if food in food_type.foods.all():
                    data['food_types'][food_type_url].append(self.food_ser(food, context=self.context(request)).data)
        data.update(common_context(request))
        return Response(data)

    def search(self, request):
        all_rests = list()
        if 'search' in request.GET:
            query = request.GET['search']
            rests = models.Restaurant.objects.all().order_by('name')
            for rest in rests:
                if query.lower() in rest.name.lower():
                    all_rests.append(rest)
        data = {'founded_rests': self.rest_ser(all_rests, many=True, context=self.context(request)).data}    # Restaurant Serializer

        data.update(common_context(request))
        return Response(data)

    def food_details(self, request, food_slug):
        food = models.Food.objects.get(slug=food_slug)
        data = {'food': self.food_ser(food, context=self.context(request)).data}

        data.update(common_context(request))
        return Response(data)








