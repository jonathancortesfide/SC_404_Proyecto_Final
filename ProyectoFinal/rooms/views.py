from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db import connection
from django.shortcuts import redirect
from django.contrib import messages

from .models import Room
from .forms import RoomForm


class RoomListView(ListView):
    model = Room
    template_name = 'rooms/list.html'
    context_object_name = 'rooms'


class RoomCreateView(CreateView):
    model = Room
    form_class = RoomForm
    template_name = 'rooms/room_form.html'
    success_url = reverse_lazy('rooms:room_list')

    def form_valid(self, form):
        hotel_id = form.cleaned_data['hotel'].id
        room_category_id = form.cleaned_data['room_category'].id
        bedsqty = form.cleaned_data['bedsqty']
        price = form.cleaned_data['price']

        try:
            with connection.cursor() as cursor:
                cursor.callproc("SP_GN_AddRoom", [
                    hotel_id,
                    room_category_id,
                    bedsqty,
                    price
                ])
            messages.success(self.request, "Room added successfully!")
        except Exception as e:
            messages.error(self.request, f"Error adding room: {e}")
            return super().form_invalid(form)

        return redirect(self.success_url)


class RoomUpdateView(UpdateView):
    model = Room
    form_class = RoomForm
    template_name = 'rooms/room_form.html'
    success_url = reverse_lazy('rooms:room_list')

    def form_valid(self, form):
        room_id = self.object.id
        hotel_id = form.cleaned_data['hotel'].id
        room_category_id = form.cleaned_data['room_category'].id
        bedsqty = form.cleaned_data['bedsqty']
        price = form.cleaned_data['price']

        try:
            with connection.cursor() as cursor:
                cursor.callproc("SP_GN_UpdateRoom", [
                    room_id,
                    hotel_id,
                    room_category_id,
                    bedsqty,
                    price
                ])
            messages.success(self.request, "Room updated successfully!")
        except Exception as e:
            messages.error(self.request, f"Error updating room: {e}")
            return super().form_invalid(form)

        return redirect(self.success_url)


class RoomDeleteView(DeleteView):
    model = Room
    template_name = 'rooms/room_confirm_delete.html'
    success_url = reverse_lazy('rooms:room_list')

    def delete(self, request, *args, **kwargs):
        room = self.get_object()
        try:
            with connection.cursor() as cursor:
                cursor.callproc("SP_GN_DeleteRoom", [room.id])
            messages.success(self.request, "Room deleted successfully!")
        except Exception as e:
            messages.error(self.request, f"Error deleting room: {e}")
            return redirect(self.success_url)

        return redirect(self.success_url)
