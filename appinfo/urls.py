from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('', base, name="base"),
    path('about', about, name="about"),
]