from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import list_companies, post_company, search_company_form, get_company, list_delete_companies, delete_companies, delete_companies_success

urlpatterns = [
    path('listcompanies', list_companies, name="list_companies"),
    path('postcompanies', post_company, name="post_companies"),
    path('searchcompany', search_company_form, name="search_company"),
    path('getcompany',get_company,  name="get_company"),
    path('listdeletecompanies', list_delete_companies, name='list_delete_companies'),
    path('deletecompanies', delete_companies, name='delete_companies'),
    path('deletecompaniessuccess', delete_companies_success, name='delete_companies_success'),
]