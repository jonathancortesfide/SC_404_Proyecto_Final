from django.shortcuts import render, get_object_or_404, redirect
from .models import RoomReservation
from .forms import RoomReservationForm

def reservation_list(request):
    reservations = RoomReservation.objects.all()
    return render(request, 'reservations/reservation_list.html', {'reservations': reservations})

def reservation_create(request):
    form = RoomReservationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('reservation_list')
    return render(request, 'reservations/reservation_form.html', {'form': form})

def reservation_update(request, pk):
    reservation = get_object_or_404(RoomReservation, pk=pk)
    form = RoomReservationForm(request.POST or None, instance=reservation)
    if form.is_valid():
        form.save()
        return redirect('reservation_list')
    return render(request, 'reservations/reservation_form.html', {'form': form})

def reservation_delete(request, pk):
    reservation = get_object_or_404(RoomReservation, pk=pk)
    if request.method == 'POST':
        reservation.delete()
        return redirect('reservation_list')
    return render(request, 'reservations/reservation_confirm_delete.html', {'reservation': reservation})
