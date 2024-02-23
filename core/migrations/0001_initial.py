# Generated by Django 5.0.1 on 2024-02-23 11:04

import django_mysql.models
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resturaunt', models.CharField(choices=[('Harrogate', 'Harrogate'), ('Leeds', 'Leeds'), ('Knaresborough Castle', 'Knaresborough Castle')], default='Harrogate', max_length=50)),
                ('date_time', models.DateTimeField(blank=True, default=None, null=True)),
                ('people', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=50)),
                ('fname', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(default='', max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region='GB')),
            ],
            options={
                'verbose_name': 'Booking',
                'verbose_name_plural': 'Bookings',
            },
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(blank=True, default=None, null=True)),
                ('fname', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(default='', max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region='GB')),
            ],
            options={
                'verbose_name': 'Class',
                'verbose_name_plural': 'Classes',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='', max_length=254)),
                ('resturaunt', models.CharField(choices=[('Harrogate', 'Harrogate'), ('Leeds', 'Leeds'), ('Knaresborough Castle', 'Knaresborough Castle')], default='Harrogate', max_length=50)),
                ('items', django_mysql.models.ListTextField(models.CharField(max_length=100), size=200)),
            ],
            options={
                'verbose_name': 'Menu Order',
                'verbose_name_plural': 'Menu Orders',
            },
        ),
    ]
