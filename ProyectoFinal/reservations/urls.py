from django.urls import path
from . import views

app_name = "reservations"
urlpatterns = [
    path('', views.reservation_list, name='reservation_list'),
    path('new/', views.reservation_create, name='reservation_create'),
    path('<int:pk>/edit/', views.reservation_update, name='reservation_update'),
    path('<int:pk>/delete/', views.reservation_delete, name='reservation_delete'),
]
