from django.shortcuts import render
from . import forms

def index(request):
    return render(request, "home/index.html")

def agregar_perro(request):
    form = forms.PerroForm(request.POST)
    context={"form": form}
    return render(request, "home/agregar_perro.html", context)

