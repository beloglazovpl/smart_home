# Generated by Django 4.0.3 on 2022-03-14 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0003_alter_sensor_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Measurment',
            new_name='Measurement',
        ),
    ]
