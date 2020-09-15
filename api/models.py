from django.db import models
from django.contrib.auth.models import User
from p4backend import settings


class Movie(models.Model):
    image = models.URLField()
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name_plural = 'movies'

    def __str__(self):
        return self.title


class Link(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='links', on_delete=models.CASCADE)
    outlet = models.CharField(max_length=20)
    link = models.URLField()
    is_public = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'links'

    def __str__(self):
        return self.outlet
