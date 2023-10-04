from django.shortcuts import render, HttpResponse
from .models import Company
from .forms import FormCompany

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
            comp = Company(nombre = data["nombre"], rubro = data["rubro"], mail = data["mail"], escliente = data["escliente"])
            comp.save()
            instance = Company.objects.all()
            context = {"instances": instance}

            return render(req, "listcompanies.html", context)
        
        else:
            
            return render(req, "postcompanies.html", {"formulario1": formulario1})             
    else:
        
        formulario1 = FormCompany()
        return render(req, "postcompanies.html", {"formulario1": formulario1})


def search_company_form(req):

        return render(req, "searchcompany.html")

def get_company(req: HttpResponse):
    nom = req.GET["nombre"]  # Use get() method with parentheses

    if nom:
        instance = Company.objects.filter(nombre__contains=nom)
        context = {"instances": instance}
        return render(req, "searchresult.html", context)
    else:
        return HttpResponse("Debe agregar una camada")
    
def delete_company(req, id):

#    print (req.method)

    if req.method == 'POST':

        comp = Company.objects.get(id = id)
        comp.delete()

        comp = Company.objects.all()
        
        return render(req, "list_companies.html")

