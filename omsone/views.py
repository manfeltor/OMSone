from django.shortcuts import render

def custom_404(req, exception):
    
    return render(req, '404.html', status=404)

def unauthlog(req):

    return render(req, "unauthlog.html")