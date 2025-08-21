from django.db import models
from users.models import Person

class Customer(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, db_column='PERSONID')
    reservation_count = models.IntegerField(db_column='RESERVATIONCOUNT')

    class Meta:
        db_table = "COSTUMER"
        managed = False

    def __str__(self):
        return f"{self.person.name} (Reservations: {self.reservation_count})"
