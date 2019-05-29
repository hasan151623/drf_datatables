from django.contrib import admin

from example.albums.models import Genre, Artist, Album


admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Album)
