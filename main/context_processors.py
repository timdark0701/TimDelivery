from . import models
from cart.cart import Cart


def common_context(request):
    context = dict()

    # List of all cities
    all_cities = models.City.objects.all()
    context['all_cities'] = all_cities

    # Current user
    user = request.user
    context['user'] = user

    # Current city
    if 'city_id' in request.session:
        current_city = models.City.objects.get(pk=request.session['city_id'])
        context['city'] = current_city

    context['cart'] = Cart(request)
    return context
