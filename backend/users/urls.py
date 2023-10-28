from django.urls import path
from .views import UserCreate, AttendeeCreate

urlpatterns = [
    path('register/', UserCreate.as_view(), name='host_register'),
    path('attendee/', AttendeeCreate.as_view(), name='attendee_register'),
]
