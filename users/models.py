from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=255, default='', blank=True)
    address = models.CharField(max_length=255, default='', blank=True)
    postal_code = models.CharField(max_length=20, default='')
    phone = models.CharField(max_length=255, default='', blank=True)

    class Meta:
        ordering = ('city',)
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'

    def __str__(self):
        return self.user.first_name
