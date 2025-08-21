from django import forms
from .models import RoomReservation

class RoomReservationForm(forms.ModelForm):
    class Meta:
        model = RoomReservation
        fields = ['room', 'customer', 'check_in_date', 'check_out_date', 'price', 'comment']
        widgets = {
            'check_in_date': forms.DateInput(attrs={'type': 'date'}),
            'check_out_date': forms.DateInput(attrs={'type': 'date'}),
        }
