from rest_framework import viewsets
from . import serializers
from ..models import Profile
from django.contrib.auth.models import User
from main.context_processor_api import common_context
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework import permissions
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer


class UserActionsView(viewsets.ViewSet):
    prof_ser = serializers.ProfileSerializer
    user_ser = serializers.UserSerializer

    def context(self, request):
        return {'request': request}

    def profile_view(self, request):
        if request.user is not None and request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)
            data = {'profile': self.prof_ser(profile, context=self.context(request)).data}

            data.update(common_context(request))
            return Response(data)
        else:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

    def login(self, request):
        username = request.data['username']
        password = request.data['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('homepage_api')
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return redirect('login_api')

    def logout(self, request):
        logout(request)
        return redirect('homepage_api')


class ProfileEditView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.ProfileEditSerializer


class RegisterAPIView(CreateAPIView):
    model = User
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.RegistrationSerializer
