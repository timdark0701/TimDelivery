from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


@admin.register(models.FoodType)
class FoodTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


@admin.register(models.Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'mini_description', 'open', 'open_time', 'close_time']
    list_filter = ['open']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


@admin.register(models.RestaurantType)
class RestaurantTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}