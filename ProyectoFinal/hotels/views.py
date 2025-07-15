from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Hotel

class HotelListView(ListView):
    model = Hotel
    template_name = 'hotels/hotel_list.html'

class HotelDetailView(DetailView):
    model = Hotel
    template_name = 'hotels/hotel_detail.html'

class HotelCreateView(CreateView):
    model = Hotel
    fields = ['name', 'description']
    template_name = 'hotels/hotel_form.html'
    success_url = reverse_lazy('hotel_list')

class HotelUpdateView(UpdateView):
    model = Hotel
    fields = ['name', 'description']
    template_name = 'hotels/hotel_form.html'
    success_url = reverse_lazy('hotel_list')

class HotelDeleteView(DeleteView):
    model = Hotel
    template_name = 'hotels/hotel_confirm_delete.html'
    success_url = reverse_lazy('hotel_list')
