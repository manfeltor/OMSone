from django import forms
from .models import Company

class FormCompany(forms.Form):

    nombre = forms.CharField(max_length=100)
    rubro = forms.CharField(max_length=20)
    mail = forms.EmailField(empty_value="vacio", error_messages={'invalid':"por favor ingresa un mail valido", 'required' : "por favor, ingresa un mail valido"})
    escliente = forms.BooleanField(required=False)

