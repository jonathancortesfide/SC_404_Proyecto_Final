from django.urls import path
from . import views

app_name = "supplies"
urlpatterns = [
    path('', views.supply_list, name='supply_list'),
]
