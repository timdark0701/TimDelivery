from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from users import views as users_views

app_name = 'main'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('set_city/<city_id>/', views.set_city, name='set_city'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', users_views.register, name='register'),
    path('profile/', users_views.profile_view, name='profile'),
    path('profile/edit/', users_views.profile_edit, name='profile_edit'),
    path('restaurant/<rest_slug>/', views.restaurant_details, name='restaurant_details'),
    path('search/', views.search, name='search'),
    path('food/<food_slug>/', views.food_details, name='food_details'),
]