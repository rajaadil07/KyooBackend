from django.urls import path
from .views import SongSearchView, SongListView

urlpatterns = [
    path('search/', SongSearchView.as_view(), name='song_search'),
    path('', SongListView.as_view(), name='song-list'),
]
