from django.db import models

class BedCategory(models.Model):
    category = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Bed Categories"
        db_table = "BEDCATEGORY"
        managed = False

    def __str__(self):
        return self.category
