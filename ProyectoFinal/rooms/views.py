from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Room  # Asegúrese de que el modelo se llama Room
from .forms import RoomForm

class RoomListView(ListView):
    model = Room
    template_name = 'rooms/room_list.html'
    context_object_name = 'rooms'

class RoomCreateView(CreateView):
    model = Room
    form_class = RoomForm
    template_name = 'rooms/room_form.html'
    success_url = '/rooms/'


class RoomUpdateView(UpdateView):
    model = Room
    fields = ['hotel', 'room_category', 'beds_qty', 'price']
    template_name = 'rooms/room_form.html'
    success_url = reverse_lazy('rooms:room_list')

class RoomDeleteView(DeleteView):
    model = Room
    template_name = 'rooms/room_confirm_delete.html'
    success_url = reverse_lazy('rooms:room_list')
