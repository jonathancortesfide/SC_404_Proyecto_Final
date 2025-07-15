from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

class UserRole(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=50)
    role = models.ForeignKey(UserRole, on_delete=models.CASCADE)

    def __str__(self):
        return self.username