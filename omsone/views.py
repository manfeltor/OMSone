from django.shortcuts import render
from django.contrib.auth.models import User

def custom_404(req, exception):
    
    return render(req, '404.html', status=404)

def unauthlog(req):

    return render(req, "unauthlog.html")
