from django.db import models
from django_mysql.models import ListTextField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class Booking(models.Model):
    CHOICES = (('Harrogate', 'Harrogate'),('Leeds', 'Leeds'),('Knaresborough Castle', 'Knaresborough Castle'))
    resturaunt = models.CharField(max_length=50,choices=CHOICES, default = 'Harrogate')

    date_time = models.DateTimeField(null=True, default=None, blank=True)
    People = (('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'))
    people = models.CharField(max_length=50,choices=People, default = '1')  
    fname = models.CharField(max_length = 50, default='')
    email = models.EmailField(default='')
    phone = models.CharField(blank=True,max_length=13)


    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'
        
    def __str__(self):
        return self.email
    
class Classes(models.Model):
    date_time = models.DateTimeField(null=True, default=None, blank=True)
    fname = models.CharField(max_length=50, default='')
    email = models.EmailField(default='')
    phone = models.CharField(blank=True,max_length=13)


    class Meta:
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'

    def __str__(self):
        return self.email
    
class Menu(models.Model):
    email = models.EmailField(default='')
    CHOICES = (('Harrogate', 'Harrogate'),('Leeds', 'Leeds'),('Knaresborough Castle', 'Knaresborough Castle'))
    resturaunt = models.CharField(max_length=50,choices=CHOICES, default = 'Harrogate')
    items = ListTextField(
        base_field=models.CharField(max_length=255),
        size=200,  # Maximum of 200 ids in list
    )
    prices = models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)

    # Add prices

    class Meta:
        verbose_name = 'Menu Order'
        verbose_name_plural = 'Menu Orders'

    def __str__(self):
        return self.email
    
    
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password,first_name,last_name):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password,first_name,last_name):
        user = self.create_user(
            email=email,
            first_name = first_name,
            last_name = last_name,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    
class MyUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email