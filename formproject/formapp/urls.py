from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),          # Root URL → form page
    path("show", views.show_details, name="show"),  # Form submission POST handler
]
