from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models

class PerroForm(forms.ModelForm):
    class Meta:
        model = models.Perro
        fields = "__all__"
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-field'}),
            'raza': forms.TextInput(attrs={'class': 'form-field'}),
            
        }

class GatoForm(forms.ModelForm):
    class Meta:
        model = models.Gato
        fields = "__all__"
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-field'}),
            'raza': forms.TextInput(attrs={'class': 'form-field'}),
           
        }

class ExoticoForm(forms.ModelForm):
    class Meta:
        model = models.Exotico
        fields = "__all__"
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-field'}),
            'raza': forms.TextInput(attrs={'class': 'form-field'}),
            
        }

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-field'}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-field'}))
    password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput(attrs={'class': 'form-field'}))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k: "" for k in fields}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-field'}),
            
        }
