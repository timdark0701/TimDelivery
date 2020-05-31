from . import views
from rest_framework import routers
from django.urls import path, include
from users.api import views as users_views


router = routers.DefaultRouter()
router.register(r'cities', views.CityView)
router.register(r'food_types', views.FoodTypeVIew)
router.register(r'restaurant_types', views.RestaurantTypeView)
router.register(r'restaurants', views.RestaurantView)
router.register(r'ingredients', views.IngredientView)
router.register(r'foods', views.FoodView)
router.register(r'users', users_views.UserView)
router.register(r'profiles', users_views.ProfileView)
router.register(r'profile/edit', users_views.ProfileEditView)


urlpatterns = [
    path('', include(router.urls)),
    path('homepage/', views.MainView.as_view({'get': 'homepage'}), name='homepage_api'),
    path('set_city/<city_id>/', views.MainView.as_view({'get': 'set_city'}), name='set_city_api'),
    path('restaurant/<rest_slug>/', views.MainView.as_view({'get': 'restaurant_details'}), name='restaurant_details_api'),
    path('search/', views.MainView.as_view({'get': 'search'}), name='search_api'),
    path('food/<food_slug>/', views.MainView.as_view({'get': 'food_details'}), name='food_details_api'),
    path('profile/', users_views.UserActionsView.as_view({'get': 'profile_view'}), name='profile_view_api'),
    path('register/', users_views.RegisterAPIView.as_view(), name='register_api'),
    path('login/', users_views.UserActionsView.as_view({'post': 'login'}), name='login_api'),
    path('logout/', users_views.UserActionsView.as_view({'get': 'logout'}), name='logout_api'),
]

