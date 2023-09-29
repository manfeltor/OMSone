from django.shortcuts import render
from .models import Company

# Create your views here.

def list_companies(req):

    all_instances = Company.objects.all()

    return render(req, 'listcompanies.html', {'instances': all_instances})
#1! def create_company(req)