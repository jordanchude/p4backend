from rest_framework.response import Response
from rest_framework import generics, status
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

    def create(self, request, *args, **kwargs):
        movie = Movie.objects.filter(
            title=request.data.get('title'),
            user=request.user
        )

        if movie:
            msg = 'Movie with that title already exists'
            raise ValidationError(msg)
        return super().create(request)

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        queryset = Movie.objects.all().filter(user=self.request.user)
        return queryset

    def update(self, request, *args, **kwargs):
        movie = Movie.objects.get(pk=self.kwargs["pk"])
        if not request.user == movie.user:
            raise PermissionDenied(
                "You have no permissions to edit this movie"
            )
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        movie = Movie.objects.get(pk=self.kwargs["pk"])
        if not request.user == movie.user:
            raise PermissionDenied("You cannot delete this movie.")
        return Response(
            {
                'message': f'{MovieSerializer(super().destroy(request, *args, **kwargs))} has been deleted',
                'status': status.HTTP_200_OK
            }
        )

