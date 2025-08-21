from django.db import models
from hotels.models import Hotel
from roomcategories.models import RoomCategory
from statuscatalogs.models import StatusCatalog  # Asegúrese de tener esta app y modelo
from bedcategories.models import BedCategory     # Asegúrese de tener esta app y modelo


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, db_column='HOTELID')
    room_category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE, db_column='ROOMCATEGORYID')
    bedsqty = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "ROOM"
        managed = False

    def __str__(self):
        return f"Habitación {self.id} - {self.hotel.name}"


class RoomStatus(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, db_column='ROOMID')
    status = models.ForeignKey(StatusCatalog, on_delete=models.CASCADE, db_column='STATUSID')
    comment = models.TextField(blank=True)

    class Meta:
        db_table = "ROOMSTATUS"
        managed = False

    def __str__(self):
        return f"{self.room} - Estado: {self.status}"


class Bed(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, db_column='ROOMID')
    bed_category = models.ForeignKey(BedCategory, on_delete=models.CASCADE, db_column='BEDCATEGORYID')
    comment = models.TextField(blank=True)

    class Meta:
        db_table = "BED"
        managed = False

    def __str__(self):
        return f"{self.bed_category} en {self.room}"
