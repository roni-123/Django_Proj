from django.contrib import admin
from .models import Booking,Classes,Menu,MyUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):
    ordering = ['email']
    list_display=['first_name','email']
    list_filter = ('is_staff', 'is_superuser', 'groups')


# Register your models here.
admin.site.register(Booking)
admin.site.register(Classes)
admin.site.register(Menu)
admin.site.register(MyUser, UserAdmin)