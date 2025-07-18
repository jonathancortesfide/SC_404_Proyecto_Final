# Generated by Django 5.2.4 on 2025-07-15 07:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_alter_activityreservation_status'),
        ('bedcategories', '0001_initial'),
        ('roomcategories', '0002_alter_roomcategory_options'),
        ('rooms', '0001_initial'),
        ('statuscatalogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bed',
            name='bed_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bedcategories.bedcategory'),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roomcategories.roomcategory'),
        ),
        migrations.AlterField(
            model_name='roomstatus',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='statuscatalogs.statuscatalog'),
        ),
        migrations.DeleteModel(
            name='BedCategory',
        ),
        migrations.DeleteModel(
            name='RoomCategory',
        ),
        migrations.DeleteModel(
            name='StatusCatalog',
        ),
    ]
