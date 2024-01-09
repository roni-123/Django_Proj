from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "core/index.html")

def about(request):
    return render(request, "core/About.html")

def booking(request):
    return render(request, "core/Bookin.html")

def socialmedia(request):
    return render(request, "core/Social Media.html")