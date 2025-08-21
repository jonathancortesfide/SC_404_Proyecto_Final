from django.db import models
from users.models import Person
from hotels.models import Hotel

class EmployeeRole(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    class Meta:
        db_table = "EMPLOYEEROLE"
        managed = False

    def __str__(self):
        return self.name

class Employee(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, db_column='HOTELID')
    person = models.ForeignKey(Person, on_delete=models.CASCADE, db_column='PERSONID')
    role = models.ForeignKey(EmployeeRole, on_delete=models.CASCADE, db_column='ROLEID')
    start_date = models.DateField(db_column='STARTDATE')
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "EMPLOYEE"
        managed = False

    def __str__(self):
        return f"{self.person.name} - {self.role.name}"