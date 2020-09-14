from rest_framework import generics
from rest_framework import viewsets
from rest_framework.exceptions import (
    ValidationError, PermissionDenied
)

from rest_framework.permissions import IsAuthenticated, AllowAny
from api.models import Movie
from api.serializers import MovieSerializer


# CRUD OPERATIONS FOR MOVIE MODEL
class MovieViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.all().filter(user=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        movie = Movie.objects.filter(
            title=request.data.get('title'),
            user=request.user
        )

        if movie:
            msg = 'Movie with that name already exists'
            raise ValidationError(msg)
        return super().create(request)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
