#cs3141
#teamc

from django.contrib import admin

from .models import Game, Categories, Genre
# Register your models here.
admin.site.register(Game)
admin.site.register(Categories)
admin.site.register(Genre)

