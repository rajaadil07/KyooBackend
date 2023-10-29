from django.urls import path
from .views import (
    EventListCreateView, 
    EventRetrieveUpdateDestroyView, 
    EventUserListCreateView,
    EventUserRetrieveUpdateDestroyView,
    SongRequestListView,
    SongRequestUpvoteView,
    SongRequestDeleteView,
    SongRequestCreateView,
    JoinEventByPIN,
)

urlpatterns = [
    path('', EventListCreateView.as_view(), name='event-list-create'),  
    path('<int:pk>/', EventRetrieveUpdateDestroyView.as_view(), name='event-retrieve-update-destroy'),  
    path('users/', EventUserListCreateView.as_view(), name='event-user-list-create'),  
    path('users/<int:pk>/', EventUserRetrieveUpdateDestroyView.as_view(), name='event-user-retrieve-update-destroy'),
    path('song-requests/', SongRequestListView.as_view(), name='song-request-list-create'),
    path('song-requests/<int:pk>/', SongRequestDeleteView.as_view(), name='song-request-delete'),
    path('song-requests/create/', SongRequestCreateView.as_view(), name='song-request-create'),
    path('song-requests/<int:pk>/upvote/', SongRequestUpvoteView.as_view(), name='song-request-upvote'),
    path('join/', JoinEventByPIN.as_view(), name='join-event-by-pin'),
]
