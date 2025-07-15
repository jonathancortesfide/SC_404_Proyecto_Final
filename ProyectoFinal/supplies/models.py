from django.db import models
from hotels.models import Hotel

class Supplier(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    contact_person_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Supply(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    supply_name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.supply_name