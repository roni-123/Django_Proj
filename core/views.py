from django.shortcuts import render,redirect
from .models import Members
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    if request.method == "POST":
        if "Sign_up" in request.POST:
            fname = request.POST["fname"]
            lname = request.POST["lname"]
            password = request.POST["password"]
            email = request.POST["email"]
            username = email.split('@')[0]

            

            new_member = User.objects.create_user(first_name = fname,last_name = lname, email = email,password = password, username = username)
            new_member.save()

            messages.success(request,"Your account has been created")

            return redirect('/')

        if "Log_in" in request.POST:
            email = request.POST["email"]
            password = request.POST["password"]

            user = authenticate(username=email.split('@')[0],password=password)

            if user is not None:

                login(request,user)
                name = user.username
                return redirect('/', {"name":name})
            
            else:
                messages.error(request,"Wrong credentials")
                return redirect('/')


    return render(request, "core/index.html")

def signout(request):
    logout(request)
    return redirect('/')

def about(request):
    return render(request, "core/About.html")

def booking(request):
    return render(request, "core/Booking.html")

def socialmedia(request):
    return render(request, "core/Social Media.html")

def menu(request):
    return render(request, "core/menu.html")