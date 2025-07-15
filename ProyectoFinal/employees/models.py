from django.db import models
from users.models import Person
from hotels.models import Hotel

class EmployeeRole(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    role = models.ForeignKey(EmployeeRole, on_delete=models.CASCADE)
    start_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.person.name} - {self.role.name}"