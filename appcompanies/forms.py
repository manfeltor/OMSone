from django import forms
from .models import Company

class FormCompany(forms.Form):

    nombre = forms.CharField(max_length=100)
    rubro = forms.CharField(max_length=20)
    mail = forms.EmailField(empty_value="vacio")
    escliente = forms.BooleanField(required=False)

class FormCompanyM(forms.ModelForm):

    class Meta:
        model=Company
        fields=("nombre", "rubro", "mail", "escliente")
