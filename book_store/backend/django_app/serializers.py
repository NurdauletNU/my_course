from django.contrib.auth.models import User
from django.core import validators
from rest_framework import serializers
from django_app import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        exclude = ["password"]
        # fields = ["username", "email"]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = "__all__"
