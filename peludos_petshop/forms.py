from django import forms
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductoForm(forms.ModelForm):

    fotoProducto = forms.FileField(required=False)

    class Meta:
        model = Producto
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
    
    username = forms.CharField(label='Nombre de usuario', min_length=5, max_length=150)  
    email = forms.EmailField(label='Correo electrónico')  
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]