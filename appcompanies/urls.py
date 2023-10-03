from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import list_companies, post_company, search_company_form, get_company

urlpatterns = [
    path('listcompanies', list_companies, name="list_companies"),
    path('postcompanies', post_company, name="post_companies"),
    path('searchcompany', search_company_form, name="search_company"),
    path('getcompany',get_company,  name="get_company"),
    
]