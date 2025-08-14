from django.db import models


class AuditLog(models.Model):
    ACTION_CHOICES = [
        ('INSERT', 'Insert'),
        ('UPDATE', 'Update'),
        ('DELETE', 'Delete'),
    ]
    
    table_name = models.CharField(max_length=100)
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    record_id = models.PositiveIntegerField()
    old_values = models.JSONField(null=True, blank=True)
    new_values = models.JSONField(null=True, blank=True)
    user_id = models.PositiveIntegerField(null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    class Meta:
        db_table = 'audit_log'
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.table_name} - {self.action} - {self.timestamp}"


class EmployeeSalaryAudit(models.Model):
    employee_id = models.PositiveIntegerField()
    old_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    new_salary = models.DecimalField(max_digits=10, decimal_places=2)
    change_date = models.DateTimeField(auto_now_add=True)
    changed_by = models.PositiveIntegerField(null=True, blank=True)
    reason = models.TextField(blank=True)

    class Meta:
        db_table = 'employee_salary_audit'
        ordering = ['-change_date']

    def __str__(self):
        return f"Empleado {self.employee_id} - Salario: {self.old_salary} → {self.new_salary}"


class RoomPriceAudit(models.Model):
    room_id = models.PositiveIntegerField()
    old_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    new_price = models.DecimalField(max_digits=10, decimal_places=2)
    change_date = models.DateTimeField(auto_now_add=True)
    changed_by = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'room_price_audit'
        ordering = ['-change_date']

    def __str__(self):
        return f"Room {self.room_id} - Price: {self.old_price} → {self.new_price}"


class ReservationAudit(models.Model):
    reservation_id = models.PositiveIntegerField()
    customer_id = models.PositiveIntegerField()
    action = models.CharField(max_length=50)
    check_in_date = models.DateField(null=True)
    check_out_date = models.DateField(null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    action_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'reservation_audit'
        ordering = ['-action_date']

    def __str__(self):
        return f"Reservation {self.reservation_id} - {self.action}"


class UserLoginAudit(models.Model):
    user_id = models.PositiveIntegerField()
    username = models.CharField(max_length=150)
    login_time = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField(blank=True)
    success = models.BooleanField(default=True)

    class Meta:
        db_table = 'user_login_audit'
        ordering = ['-login_time']

    def __str__(self):
        status = "Success" if self.success else "Failed"
        return f"{self.username} - {status} - {self.login_time}"
