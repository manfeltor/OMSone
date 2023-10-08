from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    
    username = forms.CharField(
        label="Ingresa un nombre de usuario",
        help_text="Campo requerido. Recibe hasta 150 caracteres entre letras, digitos y @/./+/-/_ unicamente"
    )
    password1 = forms.CharField(
        label="Ingresa una contraseña",
        help_text="Tu contraseña:\n*debe tener almenos 8 caracteres\n*no puede ser similar a otros de tus datos\n*no debe ser una contraseña comun (como 1234)\nno puede ser enteramente numerica"
           
    )
    password2 = forms.CharField(
        label="Confirma tu contraseña",
        help_text="Custom help text for confirm password field."
    )

    class Meta:
        model = get_user_model() 
        fields = ('username', 'password1', 'password2') 


class CustomUserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )
    
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")