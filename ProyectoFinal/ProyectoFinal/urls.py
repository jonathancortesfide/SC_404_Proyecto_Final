from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reservations/', include('reservations.urls')),
    path('activities/', include('activities.urls')),
    path('hotels/', include('hotels.urls')),
    path('rooms/', include('rooms.urls')),
    path('employees/', include('employees.urls')),
    path('supplies/', include('supplies.urls')),
    path('users/', include('users.urls')),
]
