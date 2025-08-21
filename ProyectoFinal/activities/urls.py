from django.urls import path
from .views import (
    ActivityListView,
    ActivityCreateView,
    ActivityUpdateView,
    ActivityDeleteView,
)

app_name = 'activities'

urlpatterns = [
    path('', ActivityListView.as_view(), name='activity_list'),
    path('add/', ActivityCreateView.as_view(), name='activity_create'),
    path('<int:pk>/edit/', ActivityUpdateView.as_view(), name='activity_edit'),
    path('<int:pk>/delete/', ActivityDeleteView.as_view(), name='activity_delete'),
]
