from rest_framework import serializers
from api.models import Movie, Link


class MovieSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Movie
        fields = ('id', 'user', 'image', 'title', 'description')


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('id', 'outlet', 'link')
