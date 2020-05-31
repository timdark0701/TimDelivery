from django.shortcuts import render, redirect
from .forms import OrderCreateFrom
from . import models
from cart.cart import Cart

# Create your views here.


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateFrom(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                models.OrderItem.objects.create(order=order, food=item['product'], price=item['price'],
                                                quantity=item['quantity'])
            cart.clear()
            return render(request, 'orders/created.html', {'order': order})
        else:
            return redirect('orders:order_create')
    else:
        if request.user.is_authenticated:
            form = OrderCreateFrom(instance=request.user)
        else:
            form = OrderCreateFrom()
        return render(request, 'orders/create.html', {'cart': cart, 'form': form})
