from django import forms

class FormCompany(forms.Form):

    nombre = forms.CharField(max_length=100)
    rubro = forms.CharField(max_length=20)
    mail = forms.EmailField(empty_value="vacio")
    escliente = forms.BooleanField()