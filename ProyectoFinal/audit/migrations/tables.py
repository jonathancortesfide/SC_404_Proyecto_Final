from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuditLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('table_name', models.CharField(max_length=100)),
                ('action', models.CharField(choices=[('INSERT', 'Insert'), ('UPDATE', 'Update'), ('DELETE', 'Delete')], max_length=10)),
                ('record_id', models.PositiveIntegerField()),
                ('old_values', models.JSONField(blank=True, null=True)),
                ('new_values', models.JSONField(blank=True, null=True)),
                ('user_id', models.PositiveIntegerField(blank=True, null=True)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'audit_log',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='EmployeeSalaryAudit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('employee_id', models.PositiveIntegerField()),
                ('old_salary', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('new_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('change_date', models.DateTimeField(auto_now_add=True)),
                ('changed_by', models.PositiveIntegerField(blank=True, null=True)),
                ('reason', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'employee_salary_audit',
                'ordering': ['-change_date'],
            },
        ),
        migrations.CreateModel(
            name='ReservationAudit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('reservation_id', models.PositiveIntegerField()),
                ('customer_id', models.PositiveIntegerField()),
                ('action', models.CharField(max_length=50)),
                ('check_in_date', models.DateField(null=True)),
                ('check_out_date', models.DateField(null=True)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('action_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'reservation_audit',
                'ordering': ['-action_date'],
            },
        ),
        migrations.CreateModel(
            name='RoomPriceAudit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('room_id', models.PositiveIntegerField()),
                ('old_price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('new_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('change_date', models.DateTimeField(auto_now_add=True)),
                ('changed_by', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'room_price_audit',
                'ordering': ['-change_date'],
            },
        ),
        migrations.CreateModel(
            name='UserLoginAudit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('user_id', models.PositiveIntegerField()),
                ('username', models.CharField(max_length=150)),
                ('login_time', models.DateTimeField(auto_now_add=True)),
                ('ip_address', models.GenericIPAddressField()),
                ('user_agent', models.TextField(blank=True)),
                ('success', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'user_login_audit',
                'ordering': ['-login_time'],
            },
        ),
    ]
