from django.shortcuts import render
from .models import Members
from django.contrib import messages
from django.contrib.auth import authenticate,login
# Create your views here.

def index(request):
    if request.method == "POST":
        if "Sign_in" in request.POST:
            fname = request.POST["fname"]
            email = request.POST["email"]
            password = request.POST["password"]
            conpassword = request.POST["conpassword"]

            new_member = Members(fname = fname, email = email,password = password,conpassword = conpassword)
            new_member.save()

            messages.success(request,"Your account has been created")

        if "Log_in" in request.POST:
            email = request.POST["email"]
            password = request.POST["password"]

            user = authenticate(email=email,password=password)

            if user is not None:
                login(request,user)
                name = user.fname
                return render(request, "core/index.html", {"fname":name})
            
            else:
                messages.error(request,"Wrong credentials")


    return render(request, "core/index.html")

def about(request):
    return render(request, "core/About.html")

def booking(request):
    return render(request, "core/Booking.html")

def socialmedia(request):
    return render(request, "core/Social Media.html")

def menu(request):
    return render(request, "core/menu.html")