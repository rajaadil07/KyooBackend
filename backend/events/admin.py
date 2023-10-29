from django.contrib import admin
from .models import Event, EventUser, SongRequest

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'host', 'is_active')
    search_fields = ('title', 'host')
    list_filter = ('is_active', 'date')


@admin.register(EventUser)
class EventUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'role', 'joined_at')
    search_fields = ('user__username', 'event__title')
    list_filter = ('role', 'joined_at')

@admin.register(SongRequest)
class SongRequestAdmin(admin.ModelAdmin):
    list_display = ('event', 'song', 'user', 'votes')
    search_fields = ('event__title', 'song__title', 'user__username')
    list_filter = ('votes',)
