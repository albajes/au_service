from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenVerifySerializer
from rest_framework_simplejwt.tokens import UntypedToken

from .models import User, BList
from jwt import decode


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, read_only=True)
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError('Not user with this email and password')

        return user


class CustomTokenVerifySerializer(TokenVerifySerializer):
    token = serializers.CharField()

    def validate(self, attrs):
        UntypedToken(attrs['token'])
        data = decode(attrs['token'],
                      'django-insecure-xoh@s*2w2-m@x_mmj)7obe%=ygtpg_t2q-x9d63a(8y*sddf3g',
                      algorithms=['HS256'])

        username = User.objects.get(id=data['user_id'])
        serializer = UserSerializer(username)

        return serializer.data


class BListSerializer(serializers.ModelSerializer):

    class Meta:
        model = BList
        fields = '__all__'
