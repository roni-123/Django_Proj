# import the standard Django Forms 
# from built-in library 
from django import forms  
from .models import Booking
    
# creating a form   
class TableForm(forms.ModelForm):
    
    
    class Meta: 
        model = Booking 
        fields = "__all__"
        labels = {
            'fname': ('Full Name'),
        }
        widgets = {
            'date' : forms.SelectDateWidget(empty_label="Nothing"),
            'time' : forms.TimeInput(attrs={'type': 'time'})
        }