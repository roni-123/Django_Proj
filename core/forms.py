# import the standard Django Forms 
# from built-in library 
from django import forms  
from .models import Booking
    
# creating a form   
class TableForm(forms.ModelForm): 
    fname = forms.TextInput()
    email = forms.TextInput()
    phone = forms.TextInput()
    
    class Meta: 
        model = Booking 
        fields = "__all__"
    
