from django.urls import path
from .views import (
    RoomReservationListView,
    RoomReservationCreateView,
    RoomReservationUpdateView,
    RoomReservationDeleteView,
)

app_name = 'reservations'

urlpatterns = [
    path('', RoomReservationListView.as_view(), name='roomreservation_list'),
    path('add/', RoomReservationCreateView.as_view(), name='roomreservation_create'),
    path('<int:pk>/edit/', RoomReservationUpdateView.as_view(), name='roomreservation_update'),
    path('<int:pk>/delete/', RoomReservationDeleteView.as_view(), name='roomreservation_delete'),
]
