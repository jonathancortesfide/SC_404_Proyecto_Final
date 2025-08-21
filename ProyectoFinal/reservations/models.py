from django.db import models
from rooms.models import Room
from customers.models import Customer

class RoomReservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, db_column='ROOMID')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column='COSTUMERID')
    check_in_date = models.DateField(db_column='CHECKINDATE')
    check_out_date = models.DateField(db_column='CHECKOUTDATE')
    price = models.DecimalField(max_digits=10, decimal_places=2, db_column='PRICE')
    comment = models.TextField(blank=True, db_column='COMMENTS')

    class Meta:
        db_table = "ROOMRESERVATION"
        managed = False

    def __str__(self):
        return f"{self.customer} - Room {self.room_id} ({self.check_in_date} to {self.check_out_date})"
