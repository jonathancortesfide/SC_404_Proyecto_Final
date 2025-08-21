from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db import connection
from django.shortcuts import redirect
from django.contrib import messages
from .models import RoomReservation
from .forms import RoomReservationForm
import oracledb

class RoomReservationListView(ListView):
    template_name = 'reservations/roomreservation_list.html'
    context_object_name = 'reservations'

    def get_queryset(self):
        reservations = []
        print("Starting get_queryset for RoomReservations")

        try:
            # Get the raw oracledb connection
            with connection.cursor() as django_cursor:
                cx_conn = django_cursor.connection
                print("Got raw oracledb connection:", cx_conn)

                # Create a cursor from the raw connection
                with cx_conn.cursor() as cursor:
                    # Create a REF CURSOR variable using oracledb constant
                    ref_cursor_var = cursor.var(oracledb.DB_TYPE_CURSOR)
                    
                    # Call the stored procedure
                    cursor.callproc("SP_GN_GetRoomReservations", [ref_cursor_var])

                    # Fetch rows from the OUT cursor
                    ref_cursor = ref_cursor_var.getvalue()
                    rows = ref_cursor.fetchall()

                    for row in rows:
                        reservations.append({
                            'id': row[0],
                            'room_id': row[1],
                            'bed_quantity': row[3],
                            'customer_id': row[4],
                            'customer_name': row[5],
                            'check_in_date': row[6],
                            'check_out_date': row[7],
                            'price': row[8],
                            'comments': row[9],
                        })

        except Exception as e:
            print("EXCEPTION:", e)
            messages.error(self.request, f"Error fetching reservations: {e}")

        return reservations


class RoomReservationCreateView(CreateView):
    model = RoomReservation
    form_class = RoomReservationForm
    template_name = 'reservations/roomreservation_form.html'
    success_url = reverse_lazy('reservations:roomreservation_list')

    def form_valid(self, form):
        room_id = form.cleaned_data['room'].id
        customer_id = form.cleaned_data['customer'].id
        check_in = form.cleaned_data['check_in_date']
        check_out = form.cleaned_data['check_out_date']
        price = form.cleaned_data['price']
        comment = form.cleaned_data['comment']

        try:
            with connection.cursor() as cursor:
                cursor.callproc("SP_GN_CreateRoomReservation", [
                    room_id, customer_id, check_in, check_out, price, comment
                ])
            messages.success(self.request, "Room reservation added successfully!")
        except Exception as e:
            messages.error(self.request, f"Error adding reservation: {e}")
            return super().form_invalid(form)

        return redirect(self.success_url)


class RoomReservationUpdateView(UpdateView):
    model = RoomReservation
    form_class = RoomReservationForm
    template_name = 'reservations/roomreservation_form.html'
    success_url = reverse_lazy('reservations:roomreservation_list')

    def form_valid(self, form):
        reservation_id = self.object.id
        room_id = form.cleaned_data['room'].id
        customer_id = form.cleaned_data['customer'].id
        check_in = form.cleaned_data['check_in_date']
        check_out = form.cleaned_data['check_out_date']
        price = form.cleaned_data['price']
        comment = form.cleaned_data['comment']

        try:
            with connection.cursor() as cursor:
                cursor.callproc("SP_GN_UpdateRoomReservation", [
                    reservation_id, room_id, customer_id, check_in, check_out, price, comment
                ])
            messages.success(self.request, "Room reservation updated successfully!")
        except Exception as e:
            messages.error(self.request, f"Error updating reservation: {e}")
            return super().form_invalid(form)

        return redirect(self.success_url)


class RoomReservationDeleteView(DeleteView):
    model = RoomReservation
    template_name = 'reservations/roomreservation_confirm_delete.html'
    success_url = reverse_lazy('reservations:roomreservation_list')

    def delete(self, request, *args, **kwargs):
        reservation = self.get_object()
        try:
            with connection.cursor() as cursor:
                cursor.callproc("SP_GN_DeleteRoomReservation", [reservation.id])
            messages.success(self.request, "Reservation deleted successfully!")
        except Exception as e:
            messages.error(self.request, f"Error deleting reservation: {e}")
            return redirect(self.success_url)

        return redirect(self.success_url)
