from django.db import models
from hotels.models import Hotel
from reservations.models import Customer
from rooms.models import StatusCatalog

class ActivityCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    class Meta:
        db_table = "ACTIVITYCATEGORY"
        managed = False
    

    def __str__(self):
        return self.name

class Activity(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, db_column='HOTELID')
    activity_category = models.ForeignKey(ActivityCategory, on_delete=models.CASCADE, db_column='ACTIVITYCATEGORYID')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = "Activities"
        db_table = "ACTIVITY"
        managed = False

    def __str__(self):
        return f"{self.activity_category.name} @ {self.hostel.name}"

class ActivityReservation(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE, related_name='activity_reservations')
    status = models.ForeignKey(StatusCatalog, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField(blank=True)
    attendee_qty = models.IntegerField()

    class Meta:
        verbose_name = "Activity Reservation"
        verbose_name_plural = "Activity Reservations"
