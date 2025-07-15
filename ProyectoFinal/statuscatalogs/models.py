from django.db import models

class StatusCatalog(models.Model):
    status = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.status
