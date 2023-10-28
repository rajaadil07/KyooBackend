from django.contrib import admin
from .models import Song

class SongAdmin(admin.ModelAdmin):
    list_display = ['title', 'artist', 'album']
    search_fields = ['title', 'artist', 'album']
    list_filter = ['artist', 'album']

admin.site.register(Song, SongAdmin)
