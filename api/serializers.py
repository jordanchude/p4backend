from rest_framework import serializers
from api.models import Movie, Link


class LinkSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username'
                                            '')

    class Meta:
        model = Link
        fields = ('id', 'user', 'movie', 'outlet', 'link', 'is_public')


class MovieSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    links = LinkSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Movie
        fields = ('id', 'user', 'image', 'title', 'description', 'links')