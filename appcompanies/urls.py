from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import list_companies, post_company

urlpatterns = [
    path('listcompanies.html', list_companies, name="list_companies"),
    path('postcompanies.html', post_company, name="post_companies"),
    
]