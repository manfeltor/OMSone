from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

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