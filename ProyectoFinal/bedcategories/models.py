from django.db import models

class BedCategory(models.Model):
    category = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.category
