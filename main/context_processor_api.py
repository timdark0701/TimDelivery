from .api import serializers
from . import models
from users.api import serializers as users_serializers
from cart.cart import Cart


def common_context(request):
    context = dict()

    # List of all cities
    all_cities = models.City.objects.all()
    context['all_cities'] = serializers.CitySerializer(all_cities, many=True, context={'request': request}).data

    # Current user
    user = request.user
    context['user'] = users_serializers.UserSerializer(user, context={'request': request}).data

    # Current city
    if 'city_id' in request.session:
        current_city = models.City.objects.get(pk=request.session['city_id'])
        context['current_city'] = serializers.CitySerializer(current_city, context={'request': request}).data

    cart = Cart(request)
    context['cart'] = {
            'cart_quantity': cart.__len__(),
            'cart_total': cart.get_total_cost()
        }

    return context
