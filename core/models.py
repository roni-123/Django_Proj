from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import datetime

# Create your models here.

class Booking(models.Model):
    CHOICES = (('Harrogate', 'Harrogate'),('Leeds', 'Leeds'),('Knaresborough Castle', 'Knaresborough Castle'))
    resturaunt = models.CharField(max_length=50,choices=CHOICES, default = 'Harrogate')

    date_time = models.DateTimeField(null=True, default=None, blank=True)
    People = (('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'))
    people = models.CharField(max_length=50,choices=People, default = '1')  
    fname = models.CharField(max_length=50, default='')
    email = models.EmailField(default='')
    phone = PhoneNumberField(blank=True,region="GB")


    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return self.email
    
class Classes(models.Model):
    date_time = models.DateTimeField(null=True, default=None, blank=True)
    fname = models.CharField(max_length=50, default='')
    email = models.EmailField(default='')
    phone = PhoneNumberField(blank=True,region="GB")


    class Meta:
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'

    def __str__(self):
        return self.email
    
class Menu(models.Model):
    CHOICES = (('Harrogate', 'Harrogate'),('Leeds', 'Leeds'),('Knaresborough Castle', 'Knaresborough Castle'))
    resturaunt = models.CharField(max_length=50,choices=CHOICES, default = 'Harrogate')

    


    class Meta:
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'

    def __str__(self):
        return self.email