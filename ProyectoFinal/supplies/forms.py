from django import forms
from .models import Supply

class SupplyForm(forms.ModelForm):
    class Meta:
        model = Supply
        fields = ["supplier", "supply_name", "qty", "total_price"]
