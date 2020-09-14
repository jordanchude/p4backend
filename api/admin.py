from django.contrib import admin
from api.models import Movie, Link

# Register your models here.
admin.site.register([Movie, Link])
