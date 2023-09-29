from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('listcompanies.html', list_companies, name="list_companies"),
    
]