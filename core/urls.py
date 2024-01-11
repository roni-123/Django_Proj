from django.urls import path
from core.views import *

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("booking/", booking, name="Booking"),
    path("about/", about, name="About"),
    path("social/", socialmedia, name="Social Media")
]