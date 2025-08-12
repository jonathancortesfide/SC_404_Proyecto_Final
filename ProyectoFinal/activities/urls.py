from django.urls import path
from . import views

app_name = "activities"
urlpatterns = [
    # Ruta de ejemplo
    path('', views.activity_list, name='activity_list'),
]
