from rest_framework import serializers
from ..cart import Cart


PRODUCT_QUANTITY_CHOICES = ((i, str(i)) for i in range(1, 11))


class CartUpdateSerializer(serializers.Serializer):
    quantity = serializers.ChoiceField(choices=PRODUCT_QUANTITY_CHOICES)
    update = serializers.BooleanField(required=False, style={'type': 'hidden'})