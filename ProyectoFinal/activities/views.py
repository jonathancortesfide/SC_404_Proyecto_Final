from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db import connection
from django.shortcuts import redirect
from django.contrib import messages
from collections import namedtuple
from .models import Activity
from .forms import ActivityForm
import oracledb
from django.db import connections


class ActivityListView(ListView):
    template_name = 'activities/activity_list.html'
    context_object_name = 'activities'

    def get_queryset(self):
        activities = []
        print("Starting get_queryset")

        try:
            # Get the raw oracledb connection
            with connection.cursor() as django_cursor:
                cx_conn = django_cursor.connection

                # Create a cursor from the raw connection
                with cx_conn.cursor() as cursor:
                    # Create a REF CURSOR variable using oracledb constant
                    ref_cursor_var = cursor.var(oracledb.DB_TYPE_CURSOR)

                    # Call the stored procedure
                    cursor.callproc("SP_GN_GetActivities", [ref_cursor_var])

                    # Fetch rows from the OUT cursor
                    ref_cursor = ref_cursor_var.getvalue()
                    rows = ref_cursor.fetchall()

                    for row in rows:
                        activities.append({
                            'id': row[0],
                            'hotel_id': row[1],
                            'hotel_name': row[2],
                            'activity_category_id': row[3],
                            'activity_category_name': row[4],
                            'price': row[5],
                        })

        except Exception as e:
            print("EXCEPTION:", e)
            messages.error(self.request, f"Error fetching activities: {e}")

        return activities

class ActivityCreateView(CreateView):
    model = Activity
    form_class = ActivityForm
    template_name = 'activities/activity_form.html'
    success_url = reverse_lazy('activities:activity_list')

    def form_valid(self, form):
        hotel_id = form.cleaned_data['hotel'].id
        activity_category_id = form.cleaned_data['activity_category'].id
        price = form.cleaned_data['price']

        try:
            with connection.cursor() as cursor:
                cursor.callproc("SP_GN_AddActivity", [
                    hotel_id,
                    activity_category_id,
                    price
                ])
            messages.success(self.request, "Activity added successfully!")
        except Exception as e:
            messages.error(self.request, f"Error adding activity: {e}")
            return super().form_invalid(form)

        return redirect(self.success_url)


class ActivityUpdateView(UpdateView):
    model = Activity
    form_class = ActivityForm
    template_name = 'activities/activity_form.html'
    success_url = reverse_lazy('activities:activity_list')

    def form_valid(self, form):
        activity_id = self.object.id
        hotel_id = form.cleaned_data['hotel'].id
        activity_category_id = form.cleaned_data['activity_category'].id
        price = form.cleaned_data['price']

        try:
            with connection.cursor() as cursor:
                cursor.callproc("SP_GN_UpdateActivity", [
                    activity_id,
                    hotel_id,
                    activity_category_id,
                    price
                ])
            messages.success(self.request, "Activity updated successfully!")
        except Exception as e:
            messages.error(self.request, f"Error updating activity: {e}")
            return super().form_invalid(form)

        return redirect(self.success_url)


class ActivityDeleteView(DeleteView):
    model = Activity
    template_name = 'activities/activity_confirm_delete.html'
    success_url = reverse_lazy('activities:activity_list')

    def delete(self, request, *args, **kwargs):
        activity = self.get_object()
        try:
            with connection.cursor() as cursor:
                cursor.callproc("SP_GN_DeleteActivity", [activity.id])
            messages.success(self.request, "Activity deleted successfully!")
        except Exception as e:
            messages.error(self.request, f"Error deleting activity: {e}")
            return redirect(self.success_url)

        return redirect(self.success_url)
