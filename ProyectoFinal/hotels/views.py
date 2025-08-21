from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.db import connection
from django.contrib import messages

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
    success_url = reverse_lazy('hotels:hotel_list')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        description = form.cleaned_data['description']

        try:
            with connection.cursor() as cursor:
                cursor.callproc("FN_GN_AddHotel", [name, description])
            messages.success(self.request, "Hotel added successfully!")
        except Exception as e:
            messages.error(self.request, f"Error adding hotel: {e}")
            return super().form_invalid(form)

        return redirect(self.success_url)


class HotelUpdateView(UpdateView):
    model = Hotel
    fields = ['name', 'description']
    template_name = 'hotels/hotel_form.html'
    success_url = reverse_lazy('hotels:hotel_list')

    def form_valid(self, form):
        hotel_id = self.object.id
        name = form.cleaned_data['name']
        description = form.cleaned_data['description']

        try:
            with connection.cursor() as cursor:
                cursor.callproc("FN_GN_UpdateHotel", [hotel_id, name, description])
            messages.success(self.request, "Hotel updated successfully!")
        except Exception as e:
            messages.error(self.request, f"Error updating hotel: {e}")
            return super().form_invalid(form)

        return redirect(self.success_url)


class HotelDeleteView(DeleteView):
    model = Hotel
    template_name = 'hotels/hotel_confirm_delete.html'
    success_url = reverse_lazy('hotels:hotel_list')

    def delete(self, request, *args, **kwargs):
        hotel = self.get_object()
        try:
            with connection.cursor() as cursor:
                cursor.callproc("FN_GN_DeleteHotel", [hotel.id])
            messages.success(self.request, "Hotel deleted successfully!")
        except Exception as e:
            messages.error(self.request, f"Error deleting hotel: {e}")
            return redirect(self.success_url)

        return redirect(self.success_url)
