from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db import connection
from django.shortcuts import redirect
from django.contrib import messages
from .models import Employee
from .forms import EmployeeForm
import oracledb
class EmployeeListView(ListView):
    template_name = 'employees/employee_list.html'
    context_object_name = 'employees'

    def get_queryset(self):
        employees = []
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
                    cursor.callproc("SP_GN_GetEmployees", [ref_cursor_var])

                    # Fetch rows from the OUT cursor
                    ref_cursor = ref_cursor_var.getvalue()
                    rows = ref_cursor.fetchall()

                    for row in rows:
                        employees.append({
                            'id': row[0],
                            'hotel_id': row[1],
                            'hotel_name': row[2],
                            'person_id': row[3],
                            'person_name': row[4],
                            'role_id': row[5],
                            'role_name': row[6],
                            'start_date': row[7],
                            'salary': row[8],
                        })

        except Exception as e:
            print("EXCEPTION:", e)
            messages.error(self.request, f"Error fetching employees: {e}")

        return employees


class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employees/employee_form.html'
    success_url = reverse_lazy('employees:employee_list')

    def form_valid(self, form):
        hotel_id = form.cleaned_data['hotel'].id
        person_id = form.cleaned_data['person'].id
        role_id = form.cleaned_data['role'].id
        start_date = form.cleaned_data['start_date']
        salary = form.cleaned_data['salary']

        try:
            with connection.cursor() as cursor:
                cursor.callproc("SP_GN_AddEmployee", [
                    hotel_id, person_id, role_id, start_date, salary
                ])
            messages.success(self.request, "Employee added successfully!")
        except Exception as e:
            messages.error(self.request, f"Error adding employee: {e}")
            return super().form_invalid(form)
        return redirect(self.success_url)


class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employees/employee_form.html'
    success_url = reverse_lazy('employees:employee_list')

    def form_valid(self, form):
        employee_id = self.object.id
        hotel_id = form.cleaned_data['hotel'].id
        person_id = form.cleaned_data['person'].id
        role_id = form.cleaned_data['role'].id
        start_date = form.cleaned_data['start_date']
        salary = form.cleaned_data['salary']

        try:
            with connection.cursor() as cursor:
                cursor.callproc("SP_GN_UpdateEmployee", [
                    employee_id, hotel_id, person_id, role_id, start_date, salary
                ])
            messages.success(self.request, "Employee updated successfully!")
        except Exception as e:
            messages.error(self.request, f"Error updating employee: {e}")
            return super().form_invalid(form)
        return redirect(self.success_url)


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employees/employee_confirm_delete.html'
    success_url = reverse_lazy('employees:employee_list')

    def delete(self, request, *args, **kwargs):
        employee = self.get_object()
        try:
            with connection.cursor() as cursor:
                cursor.callproc("SP_GN_DeleteEmployee", [employee.id])
            messages.success(self.request, "Employee deleted successfully!")
        except Exception as e:
            messages.error(self.request, f"Error deleting employee: {e}")
        return redirec
