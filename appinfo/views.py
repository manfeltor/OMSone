from django.shortcuts import render

# Create your views here.

def base(req):

    return render(req, "basefunc.html")

