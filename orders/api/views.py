from . import serializers
from .. import models
from rest_framework import viewsets, permissions
from django.shortcuts import redirect
from cart.cart import Cart


class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSeralizer
    permission_classes = [permissions.IsAdminUser]


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = models.OrderItem.objects.all()
    serializer_class = serializers.OrderItemSeralizer
    permission_classes = [permissions.IsAdminUser]


class OrderCreateView(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    def create(self, request):
        cart = Cart(request)
        serializer = serializers.OrderSeralizer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
            for item in cart:
                models.OrderItem.objects.create(order=order, food=item['product'], price=item['price'],
                                                quantity=item['quantity'])
            cart.clear()
            return redirect('homepage_api')