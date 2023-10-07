from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def login(req):

    if req.method == 'POST':

        formulario1 = AuthenticationForm(req, data=req.POST)
        if formulario1.is_valid():
            data = formulario1.cleaned_data
            usrn = data["username"]
            psw = data["password"]
            user = authenticate(username = usrn, password = psw)
            if user:
                return render(req, "index.html", {"msg": f"bienvenido {usrn}"})
            else:
                return render(req, "index.html", {"msg": "Datos incorrectos, revisa tus datos"})
        
        else:
            return render(req, "loginsuccess.html", {"formulario1": formulario1})           
    else:

        formulario1 = AuthenticationForm()

        return render(req, "updatecompany.html", {"formulario1": formulario1})
