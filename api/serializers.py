from .models import Movie, Link
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['urls', 'username', 'email', 'groups']


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['image', 'title', 'description']


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['outlet', 'link']
