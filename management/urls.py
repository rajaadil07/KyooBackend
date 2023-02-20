from django.urls import path
from .views import EventAPIView

urlpatterns = [
    path("events/", EventAPIView.as_view(), name='events'),
]