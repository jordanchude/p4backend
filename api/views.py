from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework import viewsets
from rest_framework.exceptions import (
    ValidationError, PermissionDenied
)

from rest_framework.permissions import IsAuthenticated, AllowAny
from api.models import Movie, Link
from api.serializers import MovieSerializer, LinkSerializer


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


# CRUD OPERATIONS FOR LINKS
class MovieLinks(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LinkSerializer

    def get_queryset(self):
        if self.kwargs.get("movie_pk"):
            movie = Movie.objects.get(pk=self.kwargs["movie_pk"])
            queryset = Link.objects.filter(
                user=self.request.user,
                movie=movie
            )
            return queryset

    def perform_create(self, serializer):
        serializer.save(user="self.request.user")


class SingleMovieLink(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LinkSerializer

    def get_queryset(self):
        # localhost:8000/categories/category_pk<1>/recipes/pk<1>/
        """
      kwargs = {
         "category_pk": 1,
         "pk": 1
      }
      """
        if self.kwargs.get("movie_pk") and self.kwargs.get("pk"):
            movie = Movie.objects.get(pk=self.kwargs["movie_pk"])
            queryset = Link.objects.filter(
                pk=self.kwargs["pk"],
                user=self.request.user,
                movie=movie
            )
            return queryset


class LinksViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = LinkSerializer

    def get_queryset(self):
        queryset = Link.objects.all().filter(user=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            raise PermissionDenied(
                "Only logged in users with accounts can create links"
            )
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        link = Link.objects.get(pk=self.kwargs["pk"])
        if not request.user == link.user:
            raise PermissionDenied(
                "You have no permissions to delete this link"
            )
        return super().destroy(request, *args, **kwargs)
