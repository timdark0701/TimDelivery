from .. import models
from rest_framework import serializers


class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.City
        fields = '__all__'


class FoodTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.FoodType
        fields = '__all__'


class RestaurantTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.RestaurantType
        fields = (
            'url',
            'name',
            'slug',
            'city',
            'restaurants'
        )


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Restaurant
        fields = (
            'url',
            'name',
            'slug',
            'rest_type',
            'image',
            'mini_description',
            'address',
            'open',
            'postal_code',
            'city',
            'open_time',
            'close_time',
            'foods',
        )


class FoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Food
        fields = '__all__'
