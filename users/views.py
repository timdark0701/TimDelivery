from django.shortcuts import render, redirect
from . import models as models
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404
from . import forms

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            profile = models.Profile.objects.create(user=user)
            profile.save()
            return redirect('main:login')
        else:
            return redirect('main:register')
    else:
        form = UserCreationForm()
        return render(request, 'users/register.html', {'form': form})


def profile_view(request):
    if request.user is not None and request.user.is_authenticated:
        profile = models.Profile.objects.get(user=request.user)
        user = request.user
        context = {'profile': profile, 'user': user}
    else:
        raise Http404('You must sign in first')
    return render(request, 'users/profile.html', context)


def profile_edit(request):
    if request.method == 'POST':
        user_form = forms.UserForm(request.POST, instance=request.user)
        profile_form = forms.ProfileForm(request.POST, instance=models.Profile.objects.get(user=request.user))

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('main:profile')
        else:
            return redirect('main:profile_edit')
    else:
        user_form = forms.UserForm(instance=request.user)
        profile_form = forms.ProfileForm(instance=models.Profile.objects.get(user=request.user))
        context = {'user_form': user_form, 'profile_form': profile_form}
        return render(request, 'users/profile_edit.html', context)