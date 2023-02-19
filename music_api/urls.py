from django.urls import path
from .views import SongAPIView

urlpatterns = [
    path("songs/",SongAPIView.as_view(),name='songs'),  
]