from django.db import models

# =====================
# GENERAL / COMMON MODELS
# =====================

class StatusCatalog(models.Model):
    status = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.status


class Person(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    birth_date = models.DateField()

    def __str__(self):
        return self.name


# =====================
# USER AND ROLE
# =====================

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


# =====================
# CUSTOMER / EMPLOYEE
# =====================

class Customer(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    reservation_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.person)


class EmployeeRole(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=100)
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


# =====================
# ROOMS / BEDS
# =====================

class RoomCategory(models.Model):
    category = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.category


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE)
    beds_qty = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Room {self.id} - {self.hotel.name}"


class RoomStatus(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    status = models.ForeignKey(StatusCatalog, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)


class BedCategory(models.Model):
    category = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.category


class Bed(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    bed_category = models.ForeignKey(BedCategory, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)


# =====================
# RESERVATIONS
# =====================

class RoomReservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"Reservation #{self.id} - {self.customer.person.name}"


# =====================
# ACTIVITIES
# =====================

class ActivityCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Activity(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    activity_category = models.ForeignKey(ActivityCategory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.activity_category.name} @ {self.hotel.name}"


class ActivityReservation(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.ForeignKey(StatusCatalog, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField(blank=True)
    attendee_qty = models.IntegerField()


# =====================
# SUPPLIERS AND SUPPLIES
# =====================

class Supplier(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    contact_person_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Supply(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    supply_name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.supply_name
