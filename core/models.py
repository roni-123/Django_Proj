from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Booking(models.Model):
    fname = models.CharField(max_length=50, default='')
    email = models.EmailField(default='')
    phone = PhoneNumberField(blank=True)


    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return self.email