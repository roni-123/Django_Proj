from django.shortcuts import render
from .models import Members
# Create your views here.

def index(request):
    if request.method == "POST":
        fname = request.POST["fname"]
        email = request.POST["email"]
        password = request.POST["password"]
        conpassword = request.POST["conpassword"]

        new_member = Members(fname = fname, email = email,password = password,conpassword = conpassword)
        new_member.save()

    return render(request, "core/index.html")

def about(request):
    return render(request, "core/About.html")

def booking(request):
    return render(request, "core/Booking.html")

def socialmedia(request):
    return render(request, "core/Social Media.html")

def menu(request):
    return render(request, "core/menu.html")