from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import list_companies, post_company, search_company_form, get_company, list_delete_companies, list_delete_employees, update_employee_success
from .views import delete_companies, delete_companies_success, update_company, post_employee_success, delete_employees_success, delete_employees
from .views import EmployeeCreateView, EmployeeListView, EmployeeDetailView, EmployeeUpdateView

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
    path('createemployee/', EmployeeCreateView.as_view(), name='post_employee'),
    path('updateemployee/<pk>', EmployeeUpdateView.as_view(), name='update_employee'),

    path('postemployeesuccess/', post_employee_success, name='post_employee_success'),
    path('listdeleteemployees/', list_delete_employees, name='list_delete_employees'),
    path('deleteemployees/', delete_employees, name='delete_employees'),
    path('deleteemployeessuccess/', delete_employees_success, name='delete_employees_success'),
    path('updateemployeesuccess/', update_employee_success, name='update_employee_success'),
]