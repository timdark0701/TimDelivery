from . import views
from rest_framework import routers
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'orders', views.OrderViewSet)
router.register(r'order/items', views.OrderItemViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('create/', views.OrderCreateView.as_view({'post': 'create'}), name='create_order_api'),
]
