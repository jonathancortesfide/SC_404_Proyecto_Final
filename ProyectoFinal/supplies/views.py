from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db import connection
from django.shortcuts import redirect
from django.contrib import messages

from .models import Supply
from .forms import SupplyForm


class SupplyListView(ListView):
    model = Supply
    template_name = 'supplies/list.html'
    context_object_name = 'supplies'


class SupplyCreateView(CreateView):
    model = Supply
    form_class = SupplyForm
    template_name = 'supplies/supply_form.html'
    success_url = reverse_lazy('supplies:supply_list')

    def form_valid(self, form):
        supplier = form.cleaned_data['supplier'].id
        name = form.cleaned_data['supply_name']
        quantity = form.cleaned_data['qty']
        price = form.cleaned_data['total_price']

        try:
            with connection.cursor() as cursor:
                cursor.callproc("SP_GN_AddSupply", [
                    supplier,
                    name,
                    quantity,
                    price
                ])
            messages.success(self.request, "Supply added successfully!")
        except Exception as e:
            messages.error(self.request, f"Error adding supply: {e}")
            return super().form_invalid(form)

        return redirect(self.success_url)


class SupplyUpdateView(UpdateView):
    model = Supply
    form_class = SupplyForm
    template_name = 'supplies/supply_form.html'
    success_url = reverse_lazy('supplies:supply_list')

    def form_valid(self, form):
        supply_id = self.object.id
        supplier_id = form.cleaned_data['supplier'].id
        name = form.cleaned_data['supply_name']
        quantity = form.cleaned_data['qty']
        price = form.cleaned_data['total_price']

        try:
            with connection.cursor() as cursor:
                cursor.callproc("SP_GN_UpdateSupply", [
                    supply_id,
                    supplier_id,
                    name,
                    quantity,
                    price
                ])
            messages.success(self.request, "Supply updated successfully!")
        except Exception as e:
            messages.error(self.request, f"Error updating supply: {e}")
            return super().form_invalid(form)

        return redirect(self.success_url)


class SupplyDeleteView(DeleteView):
    model = Supply
    template_name = 'supplies/supply_confirm_delete.html'
    success_url = reverse_lazy('supplies:supply_list')

    def delete(self, request, *args, **kwargs):
        supply = self.get_object()
        try:
            with connection.cursor() as cursor:
                cursor.callproc("SP_GN_DeleteSupply", [supply.id])
            messages.success(self.request, "Supply deleted successfully!")
        except Exception as e:
            messages.error(self.request, f"Error deleting supply: {e}")
            return redirect(self.success_url)

        return redirect(self.success_url)
