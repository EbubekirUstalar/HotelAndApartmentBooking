from django.urls import path

from .views import BookingInfoViewSet

urlpatterns = [
    path('units/', BookingInfoViewSet.as_view())
]