from rest_framework import serializers
from ..models import Profile
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            'url',
            'first_name',
            'last_name',
            'username',
            'email',
        )


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileEditSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = '__all__'


class RegistrationSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'password2'
        )

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
        )
        password = validated_data['password']
        password2 = validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password1': 'password1 and password2 must be the same.'})
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )