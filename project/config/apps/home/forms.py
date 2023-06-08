from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PerroForm(forms.ModelForm):
    class Meta:
        model = models.Perro
        fields = "__all__"

class GatoForm(forms.ModelForm):
    class Meta:
        model = models.Gato
        fields = "__all__"

class ExoticoForm(forms.ModelForm):
    class Meta:
        model = models.Exotico
        fields = "__all__"        

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k: "" for k in fields}