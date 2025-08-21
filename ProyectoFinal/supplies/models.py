from django.db import models
from hotels.models import Hotel

class Supplier(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, db_column='HOTELID')
    location = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    contact_person_name = models.CharField(max_length=100, db_column='CONTACTPERSONNAME')
    phone_number = models.CharField(max_length=20, db_column='PHONENUMBER')

    class Meta:
        db_table = "SUPPLIER"
        managed = False

    def __str__(self):
        return self.name

class Supply(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, db_column='SUPPLIERID')
    supply_name = models.CharField(max_length=100, db_column='SUPPLYNAME')
    qty = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, db_column='TOTALPRICE')

    class Meta:
        db_table = "SUPPLY"
        managed = False

    def __str__(self):
        return self.supply_name
