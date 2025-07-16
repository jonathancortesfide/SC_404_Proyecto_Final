from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name='home'),
    path('rooms/', include('rooms.urls')),
    path('hotels/', include('hotels.urls')),
    # path('employees/', include('employees.urls')),
    # path('customers/', include('customers.urls')),
    # path('supplies/', include('supplies.urls')),
    # path('activities/', include('activities.urls')),
    path('admin/', admin.site.urls),
]
