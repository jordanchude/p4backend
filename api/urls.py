from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from api.views import MovieViewSet, MovieLinks, LinksViewSet, SingleMovieLink

router = routers.DefaultRouter()
router.register('movies', MovieViewSet, basename='movies')
router.register('links', LinksViewSet, basename='links')

custom_urlpatterns = [
    url(r'movies/(?P<movie_pk>\d+)/links$', MovieLinks.as_view(), name='movie_links'),
    url(r'movies/(?P<movie_pk>\d+)/links/(?P<pk>\d+)$', SingleMovieLink.as_view(), name='single_movie_link')
]

urlpatterns = router.urls
urlpatterns += custom_urlpatterns
