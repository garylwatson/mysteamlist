#cs3141
#teamc

from django.contrib import admin

from .models import Game, Category, Genre
# Register your models here.
admin.site.register(Game)
admin.site.register(Category)
admin.site.register(Genre)

