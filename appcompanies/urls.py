from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import list_companies, post_company, search_company_form, get_company, list_delete_companies 
from .views import delete_companies, delete_companies_success, update_company
from .views import EmployeeCreateView, EmployeeListView, EmployeeDetailView, EmployeeUpdateView, EmployeeDeleteView

urlpatterns = [
    path('listcompanies/', list_companies, name="list_companies"),
    path('postcompanies/', post_company, name="post_companies"),
    path('searchcompany/', search_company_form, name="search_company"),
    path('getcompany/',get_company,  name="get_company"),
    path('listdeletecompanies/', list_delete_companies, name='list_delete_companies'),
    path('deletecompanies/', delete_companies, name='delete_companies'),
    path('deletecompaniessuccess/', delete_companies_success, name='delete_companies_success'),
    path('updatecompany/<int:id>', update_company, name='update_company'),
    
    path('listemployees/', EmployeeListView.as_view(), name='list_employees'),
    path('detailemployee/', EmployeeDetailView.as_view(), name='detail_employee'),
    path('createemployee/', EmployeeCreateView.as_view(), name='create_employee'),
    path('updateemployee/', EmployeeUpdateView.as_view(), name='update_employee'),
    path('deleteemployee/', EmployeeDeleteView.as_view(), name='delete_employee'),
]