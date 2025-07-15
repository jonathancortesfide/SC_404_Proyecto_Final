from django import forms
from .models import RoomReservation

class RoomReservationForm(forms.ModelForm):
    class Meta:
        model = RoomReservation
        fields = ['room', 'customer', 'check_in_date', 'check_out_date', 'price']
