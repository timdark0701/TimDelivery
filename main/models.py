from django.db import models
from django.urls import reverse

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=50, default='')
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)
        verbose_name = 'city'
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.name


class FoodType(models.Model):
    name = models.CharField(max_length=100, default='')
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)
        verbose_name = 'food_type'
        verbose_name_plural = 'food_types'

    def __str__(self):
        return self.name


class RestaurantType(models.Model):
    name = models.CharField(max_length=100, default='')
    slug = models.SlugField()
    city = models.ForeignKey(City, on_delete=models.CASCADE, default=1)

    class Meta:
        ordering = ('name',)
        verbose_name = 'rest_type'
        verbose_name_plural = 'rest_types'

    def __str__(self):
        return self.slug


def rest_image_folder(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return "restaurants/{}/{}".format(instance.slug, filename)


class Restaurant(models.Model):
    name = models.CharField(max_length=255, default='')
    slug = models.SlugField()
    rest_type = models.ForeignKey(RestaurantType, on_delete=models.CASCADE, related_name='restaurants')
    image = models.ImageField(upload_to=rest_image_folder, blank=True)
    mini_description = models.CharField(max_length=255, default='')
    address = models.CharField(max_length=255, default='')
    open = models.BooleanField(default=True)
    postal_code = models.CharField(max_length=16, default='')
    city = models.ForeignKey(City, on_delete=models.CASCADE, default=1)
    open_time = models.TimeField()
    close_time = models.TimeField()

    class Meta:
        ordering = ('name',)
        verbose_name = 'restaurant'
        verbose_name_plural = 'restaurants'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:restaurant_details', args=[self.slug])


def food_image_folder(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return "foods/{}/{}".format(instance.slug, filename)


class Food(models.Model):
    name = models.CharField(max_length=255, default='')
    slug = models.SlugField(unique=True)
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE, related_name='foods')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='foods')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ingredients = models.TextField()
    image = models.ImageField(upload_to=food_image_folder, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'food'
        verbose_name_plural = 'foods'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:food_details', args=[self.slug])

