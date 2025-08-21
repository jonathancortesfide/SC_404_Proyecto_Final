from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        db_table = "HOTEL"
        managed = False

    def __str__(self):
        return self.name
