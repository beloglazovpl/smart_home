# Generated by Django 4.0.3 on 2022-03-14 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_alter_sensor_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='description',
            field=models.CharField(max_length=200, verbose_name='Описание'),
        ),
    ]