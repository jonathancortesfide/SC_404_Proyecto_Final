from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db import connection
from django.shortcuts import redirect
from django.contrib import messages
from .models import Customer
from .forms import CustomerForm
import oracledb  # make sure this is installed

class CustomerListView(ListView):
    template_name = 'customers/customer_list.html'
    context_object_name = 'customers'

    def get_queryset(self):
        customers = []
        try:
            with connection.cursor() as django_cursor:
                cx_conn = django_cursor.connection
                with cx_conn.cursor() as cursor:
                    ref_cursor_var = cursor.var(oracledb.DB_TYPE_CURSOR)
                    cursor.callproc("SP_GN_GetCustomers", [ref_cursor_var])
                    ref_cursor = ref_cursor_var.getvalue()
                    rows = ref_cursor.fetchall()
                    for row in rows:
                        customers.append({
                            'id': row[0],
                            'person_id': row[1],
                            'person_name': row[2],
                            'reservation_count': row[3],
                        })
        except Exception as e:
            messages.error(self.request, f"Error fetching customers: {e}")

        return customers


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/customer_form.html'
    success_url = reverse_lazy('customers:customer_list')

    def form_valid(self, form):
        person_id = form.cleaned_data['person'].id
        reservation_count = form.cleaned_data['reservation_count']

        try:
            with connection.cursor() as cursor:
                cursor.callproc("SP_GN_AddCustomer", [person_id, reservation_count])
            messages.success(self.request, "Customer added successfully!")
        except Exception as e:
            messages.error(self.request, f"Error adding customer: {e}")
            return super().form_invalid(form)

        return redirect(self.success_url)


class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/customer_form.html'
    success_url = reverse_lazy('customers:customer_list')

    def form_valid(self, form):
        customer_id = self.object.id
        person_id = form.cleaned_data['person'].id
        reservation_count = form.cleaned_data['reservation_count']

        try:
            with connection.cursor() as cursor:
                cursor.callproc("SP_GN_UpdateCustomer", [customer_id, person_id, reservation_count])
            messages.success(self.request, "Customer updated successfully!")
        except Exception as e:
            messages.error(self.request, f"Error updating customer: {e}")
            return super().form_invalid(form)

        return redirect(self.success_url)


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customers/customer_confirm_delete.html'
    success_url = reverse_lazy('customers:customer_list')

    def delete(self, request, *args, **kwargs):
        customer = self.get_object()
        try:
            with connection.cursor() as cursor:
                cursor.callproc("SP_GN_DeleteCustomer", [customer.id])
            messages.success(self.request, "Customer deleted successfully!")
        except Exception as e:
            messages.error(self.request, f"Error deleting customer: {e}")
            return redirect(self.success_url)

        return redirect(self.success_url)
