from django.urls import path
from .views import (
    EventListCreateView, 
    EventRetrieveUpdateDestroyView, 
    EventUserListCreateView,
    EventUserRetrieveUpdateDestroyView,
    SongRequestCreateView,
    JoinEventByPIN,
)

urlpatterns = [
    path('', EventListCreateView.as_view(), name='event-list-create'),  
    path('<int:pk>/', EventRetrieveUpdateDestroyView.as_view(), name='event-retrieve-update-destroy'),  
    path('users/', EventUserListCreateView.as_view(), name='event-user-list-create'),  
    path('users/<int:pk>/', EventUserRetrieveUpdateDestroyView.as_view(), name='event-user-retrieve-update-destroy'),
    path('song-requests/', SongRequestCreateView.as_view(), name='song-request-create'),  
    path('join/', JoinEventByPIN.as_view(), name='join-event-by-pin'),
]
