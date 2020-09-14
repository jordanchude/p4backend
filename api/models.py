from django.db import models
from django.contrib.auth.models import User
from p4backend import settings


class Movie(models.Model):
    image = models.URLField(max_length=200)
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'movies'

    def __str__(self):
        return self.title


class Link(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    outlet = models.CharField(max_length=20)
    link = models.URLField(max_length=200)

    class Meta:
        verbose_name_plural = 'links'

    def __str__(self):
        return self.outlet
