from .. import models
from rest_framework import serializers


class OrderSeralizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Order
        fields = '__all__'


class OrderItemSeralizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.OrderItem
        fields = '__all__'


