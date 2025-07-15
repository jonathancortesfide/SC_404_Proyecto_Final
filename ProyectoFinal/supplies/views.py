from django.shortcuts import render
from .models import Supply

def supply_list(request):
    supplies = Supply.objects.all()
    return render(request, 'supplies/supply_list.html', {'supplies': supplies})
