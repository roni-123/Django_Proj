# Generated by Django 5.0.1 on 2024-02-19 15:23

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_booking_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='people',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=50),
        ),
        migrations.AddField(
            model_name='booking',
            name='resturaunt',
            field=models.CharField(choices=[('Harrogate', 'Harrogate'), ('Leeds', 'Leeds'), ('Knaresborough Castle', 'Knaresborough Castle')], default='Harrogate', max_length=50),
        ),
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region='GB'),
        ),
    ]