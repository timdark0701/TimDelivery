from django import forms
from . import models


class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = (
            'city',
            'address',
            'phone'
        )
