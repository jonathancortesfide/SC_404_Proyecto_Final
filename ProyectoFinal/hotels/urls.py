from django.urls import path
from .views import (
    HotelListView, HotelDetailView, HotelCreateView,
    HotelUpdateView, HotelDeleteView
)

urlpatterns = [
    path('', HotelListView.as_view(), name='hotel_list'),
    path('<int:pk>/', HotelDetailView.as_view(), name='hotel_detail'),
    path('new/', HotelCreateView.as_view(), name='hotel_create'),
    path('<int:pk>/edit/', HotelUpdateView.as_view(), name='hotel_update'),
    path('<int:pk>/delete/', HotelDeleteView.as_view(), name='hotel_delete'),
]
