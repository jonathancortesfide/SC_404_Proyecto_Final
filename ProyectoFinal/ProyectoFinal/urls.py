from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),  # su home actual
    path('rooms/', include('rooms.urls', namespace='rooms')),
    path('hotels/', include('hotels.urls', namespace='hotels')),
    path('supplies/', include('supplies.urls', namespace='supplies')),
    path('activities/', include('activities.urls', namespace='activities')),
    path('employees/', include('employees.urls', namespace='employees')),
    path('clients/', include('users.urls', namespace='clients')),   # “Clientes”
]
