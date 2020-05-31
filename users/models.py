from django.db import models
from django.contrib.auth.models import User
from main.models import City
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE, default=1)
    address = models.CharField(max_length=255, default='', blank=True)
    phone = models.CharField(max_length=255, default='', blank=True)

    class Meta:
        ordering = ('city',)
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'

    def __str__(self):
        return self.user.first_name
