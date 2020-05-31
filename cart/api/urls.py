from django.urls import path
from . import views


urlpatterns = [
    path('details/', views.CartView.as_view({'get': 'details'}), name='cart_details_api'),
    path('add/<food_slug>/', views.CartView.as_view({'get': 'add'}), name='cart_add_api'),
    path('update/<food_slug>/', views.CartView.as_view({'post': 'update'}), name='cart_update_api'),
    path('remove/<food_slug>/', views.CartView.as_view({'get': 'remove'}), name='cart_remove_api'),
]