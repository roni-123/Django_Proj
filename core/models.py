from django.db import models

# Create your models here.

class Members(models.Model):
    fname = models.CharField(max_length=50, default='')
    email = models.EmailField(default='')
    password = models.CharField(max_length=50, default='')
    conpassword = models.CharField(max_length=50, default='')

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'

    def __str__(self):
        return self.email