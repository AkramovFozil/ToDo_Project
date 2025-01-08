from django.contrib.auth.backends import UserModel
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User


class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'

    def validate(self, attrs):
        authenticate_kwargs = {
            self.username_field: attrs[self.username_field],
            'password': attrs['password'],
        }
        try:
            authenticate_kwargs['request'] = self.context['request']
        except KeyError:
            pass

        user = authenticate(**authenticate_kwargs)

        if user is None or not user.is_active:
            raise serializers.ValidationError(
                'No active account found with the given credentials'
            )

        data = super().validate(attrs)
        return data


class UserRegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')

    def create(self, validated_data):
        return User.objects.create_user(email=validated_data['email'],password=validated_data['password'])