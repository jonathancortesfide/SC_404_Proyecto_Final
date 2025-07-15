from django.urls import path
from . import views

urlpatterns = [
    path('', views.supply_list, name='supply_list'),
]
