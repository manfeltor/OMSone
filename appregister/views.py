from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm, CustomUserEditForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


# Create your views here.

def login1(req):

    if req.method == 'POST':

        formulario1 = AuthenticationForm(req, data=req.POST)
        if formulario1.is_valid():
            data = formulario1.cleaned_data
            usrn = data["username"]
            psw = data["password"]
            user = authenticate(username = usrn, password = psw)
            if user:

                login(req, user)
                return render(req, "loginsuccess.html", {"msg": "1", "usr": usrn})
            else:
                
                return render(req, "loginsuccess.html", {"msg": "0"})

        else:
            
            return render(req, "loginsuccess.html", {"msg": "0"})
                
    else:

        user=req.user
        formulario1 = AuthenticationForm()

        return render(req, "login.html", {"formulario1": formulario1})

@login_required    
def registration(req):

    if req.method == 'POST':

        formulario1 = CustomUserCreationForm(req.POST)
        if formulario1.is_valid():
            data = formulario1.cleaned_data
            usrn = data["username"]
            formulario1.save()

            return render(req, "registrationsuccess.html", {"username":usrn, "status":"1"})
        else:
            return render(req, "registrationsuccess.html", {"status":"0"})

    else:
        formulario1 = CustomUserCreationForm()
        return render(req, "registration.html", {"instance":formulario1})


def list_registered_users(req):

    users = User.objects.all()

    return render(req, "listusers.html", {"instances": users})

@login_required
def list_delete_users(req):

    all_instances = User.objects.all()

    return render(req, "listdeleteusers.html", {'instances': all_instances})

@login_required
def delete_users(req):
    if req.method == 'POST':
        selected_instances_ids = req.POST.getlist('selected_instances')
        instances_to_delete = User.objects.filter(id__in=selected_instances_ids)
        instances_to_delete.delete()
    return HttpResponseRedirect(reverse_lazy('delete_users_success'))

def delete_users_success(req):

    all_instances = User.objects.all()

    return render(req, "deleteuserssuccess.html", {'instances': all_instances})

@login_required
def update_user(req):
    usr = req.user
    if req.method == 'POST':

        formulario1 = CustomUserEditForm(req.POST, instance=req.user)
        if formulario1.is_valid():
            
            data = formulario1.cleaned_data
            usr.first_name = data["first_name"]
            usr.last_name = data["last_name"]
            usr.email = data["email"]
            usr.save()
            return render(req, "updateusersuccess.html", {"usnm": usr})
        
        else:
            return render(req, "updateusersuccess.html", {"usnm": "0"})

    else:

        formulario1 = CustomUserEditForm(instance=usr)
        return render(req, "updateuser.html", {"instance":formulario1})
