from django.db import models

class RoomCategory(models.Model):
    name = models.CharField(max_length=100, db_column='CATEGORY')
    description = models.TextField(blank=True)

    class Meta:
        db_table = "ROOMCATEGORY"
        managed = False
        verbose_name = "Room Category"
        verbose_name_plural = "Room Categories"
    def __str__(self):
        return self.name

