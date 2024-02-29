from django.shortcuts import render,redirect
from .forms import TableForm,ClassForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import Menu

# Create your views here.

def index(request):
    context = {}
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
                name = request.user.username
                print(name)
                context['name'] = name
                return redirect('/')
            
            else:
                messages.error(request,"Wrong credentials")
                return redirect('/')


    return render(request, "core/index.html",context)

def signout(request):
    logout(request)
    return redirect('/')

def about(request):
    return render(request, "core/About.html")

def booking(request):
    if request.method == "POST":
        if "booking" in request.POST:
            form = TableForm(request.POST,request.FILES)
            # check whether it's valid:
            if form.is_valid():
                messages.success(request,"Your order has been created")
                # process the data in form.cleaned_data as required
                form.save()
                return redirect("/booking/")        
        
        elif "class" in request.POST:
            form = ClassForm(request.POST,request.FILES)
            print(request.FILES)
            # check whether it's valid:
            if form.is_valid():
                messages.success(request,"Your order has been created")

                # process the data in form.cleaned_data as required
                form.save()
            print(form.errors)

            return redirect("/booking/")
        
        elif "menu" in request.POST:
            resturaunt = request.POST['Location']
            menitems,prices = [],0.0
            for items in request.POST.getlist('items[]'):
                items = items.split(",")
                menitems.append(items[0])
                prices += float(items[1])

            #
            #try:
            #    menitems = request.POST.getlist('items[]')
            #except:
            #    messages.error(request,"Did not enter an item")
            #    return redirect("/booking/")
            #
                
            print(menitems)

            email = request.POST['email3']
            item = Menu(email = email,items = menitems ,prices = prices,resturaunt =resturaunt)
            item.save()
            messages.success(request,"Your order has been created")
            return redirect("/booking/")

    context = {
        'table_form' : TableForm(),
        'class_form' : ClassForm(),
    }
    
    return render(request, "core/Booking.html",context)

def socialmedia(request):
    return render(request, "core/Social Media.html")

def menu(request):
    return render(request, "core/menu.html")