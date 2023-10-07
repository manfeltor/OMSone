from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .models import Company, Employee
from .forms import FormCompany
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

# Create your views here.

def list_companies(req):

    all_instances = Company.objects.all()

    return render(req, 'listcompanies.html', {'instances': all_instances})

 
def post_company(req):

#    print (req.method)

    if req.method == 'POST':

        formulario1 = FormCompany(req.POST)
        if formulario1.is_valid():
            data = formulario1.cleaned_data
            comp = Company(nombre = data["nombre"], rubro = data["rubro"], mail = data["mail"], escliente=data.get("escliente", False))
            comp.save()
            instance = Company.objects.all()
            context = {"instances": instance}

            return render(req, "postcompaniessuccess.html", context)
        
        else:
            
            return render(req, "postcompanies.html", {"formulario1": formulario1})             
    else:
        
        formulario1 = FormCompany()
        return render(req, "postcompanies.html", {"formulario1": formulario1})


def search_company_form(req):

        return render(req, "searchcompany.html")


def get_company(req: HttpResponse):
    nom = req.GET["nombre"]

    if nom:
        instance = Company.objects.filter(nombre__contains=nom)
        context = {"instances": instance}
        return render(req, "searchresult.html", context)
    else:
        return HttpResponse("Debe agregar una camada")
    

def list_delete_companies(req):

    all_instances = Company.objects.all()
    
    return render(req, "deletecompanies.html", {'instances': all_instances})


def delete_companies(req):
    if req.method == 'POST':
        selected_instances_ids = req.POST.getlist('selected_instances')
        instances_to_delete = Company.objects.filter(id__in=selected_instances_ids)
        instances_to_delete.delete()
    return HttpResponseRedirect(reverse_lazy('delete_companies_success'))
    

def delete_companies_success(req):

    all_instances = Company.objects.all()

    return render(req, "deletecompaniessuccess.html", {'instances': all_instances})


def update_company(req, id):

    compup = Company.objects.get(id=id)
    if req.method == 'POST':
        formulario1 = FormCompany(req.POST)
        if formulario1.is_valid():
            print("2")
            data = formulario1.cleaned_data
            compup.nombre = data["nombre"]
            compup.rubro = data["rubro"]
            compup.mail = data["mail"]
            compup.escliente = data["escliente"]
            compup.save()
            instance = Company.objects.get(id=id)
            context = {"instances": instance}
            print(instance)

            return render(req, "updatecompanysuccess.html", context)
        
        else:
            return render(req, "updatecompany.html", {"formulario1": formulario1})             
    else:
        formulario1 = FormCompany(initial={
            "nombre" : compup.nombre,
            "rubro": compup.rubro,
            "mail": compup.mail,
            "escliente": compup.escliente,
        })
        return render(req, "updatecompany.html", {"formulario1": formulario1, "id":compup.id})
    

class EmployeeListView(ListView):
    model = Employee
    template_name = "listemployees.html"
    context_object_name = "instances"

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = "detailemployee.html"
    context_object_name = "empleado"

class EmployeeCreateView(CreateView):
    model = Employee
    template_name = "postemployee.html"
    fields = ["nombre", "apellido", "empresa"]
    success_url = reverse_lazy('post_employee_success')

class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = "updateemployee.html"
    fields = '__all__'
    context_object_name = "instance"
    success_url = reverse_lazy('update_employee_success')

def post_employee_success(req):

    context = Employee.objects.all()

    return render(req, 'postemployeesuccess.html', {"instances":context})

def update_employee_success(req):

    context = Employee.objects.all()

    return render(req, 'updateemployeesuccess.html', {"instances":context})

def list_delete_employees(req):

    all_instances = Employee.objects.all()
    
    return render(req, "deleteemployees.html", {'instances': all_instances})

def delete_employees(req):
    if req.method == 'POST':
        selected_instances_ids = req.POST.getlist('selected_instances')
        instances_to_delete = Employee.objects.filter(id__in=selected_instances_ids)
        instances_to_delete.delete()
    return HttpResponseRedirect(reverse_lazy('delete_employees_success'))
    
def delete_employees_success(req):

    all_instances = Employee.objects.all()

    return render(req, "deleteemployeessuccess.html", {'instances': all_instances})

