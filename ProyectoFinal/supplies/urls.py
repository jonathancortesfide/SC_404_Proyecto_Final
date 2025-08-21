from django.urls import path
from . import views
from .views import SupplyCreateView

app_name = 'supplies'

urlpatterns = [
    path('', views.SupplyListView.as_view(), name='supply_list'),
    path('new/', SupplyCreateView.as_view(), name='supply_create'),
    path('<int:pk>/edit/', views.SupplyUpdateView.as_view(), name='supply_update'),
    path('<int:pk>/delete/', views.SupplyDeleteView.as_view(), name='supply_delete'),
]
