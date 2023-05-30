from django import forms
from . import models

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