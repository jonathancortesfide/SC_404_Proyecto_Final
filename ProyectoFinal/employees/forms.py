from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    start_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control'}
        ),
        label="Fecha de Inicio"
    )

    class Meta:
        model = Employee
        fields = ['hotel', 'person', 'role', 'start_date', 'salary']
