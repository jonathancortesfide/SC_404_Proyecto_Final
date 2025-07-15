from django.db import models
from hotels.models import Hotel
from reservations.models import Customer
from rooms.models import StatusCatalog

class ActivityCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Activity(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    activity_category = models.ForeignKey(ActivityCategory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.activity_category.name} @ {self.hostel.name}"

class ActivityReservation(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    customer = models.ForeignKey('reservations.Customer', on_delete=models.CASCADE, related_name='activity_reservations')
    status = models.ForeignKey(StatusCatalog, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField(blank=True)
    attendee_qty = models.IntegerField()
