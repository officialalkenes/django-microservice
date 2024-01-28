from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer, UserSerializer
from djoser.serializers import TokenCreateSerializer
from rest_framework import serializers


User = get_user_model()


class CreateUserSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "phone_number")


class CustomUserSerializer(UserSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "phone_number",
        )
