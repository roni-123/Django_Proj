# import the standard Django Forms 
# from built-in library 
from django import forms  
from .models import Booking,Classes
from django.contrib.admin import widgets
    
# creating a form   
class TableForm(forms.ModelForm):
    
    
    class Meta: 
        model = Booking 
        fields = "__all__"
        labels = {
            'fname': ('Full Name'),
            'date_time' : ('Date & Time'),
        }
        widgets = {
            'resturaunt' : forms.Select(attrs={'style':'width: 100px; text-align: center;margin-bottom: 10px'}),
            'date_time' : forms.SplitDateTimeWidget(date_attrs={"type": "date"}, time_attrs={"type": "time","interval": "30"})
        }
        field_classes={
            'date_time' : forms.SplitDateTimeField
        }

class ClassForm(forms.ModelForm):
    
    class Meta: 
        model = Classes 
        fields = "__all__"
        labels = {
            'fname': ('Full Name'),
            'date_time' : ('Date & Time'),
        }
        widgets = {
            'date_time' : forms.SplitDateTimeWidget(date_attrs={"type": "date"}, time_attrs={"type": "time","interval": "30"})
        }
        field_classes={
            'date_time' : forms.SplitDateTimeField
        }


