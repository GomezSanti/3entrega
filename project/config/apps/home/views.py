from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages


def index(request):
    return render(request, "home/index.html")

def agregar_perro(request):
    if request.method == "POST":
        form = forms.PerroForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Ya contamos con los datos de nuestro amiguite, ¡pronto te llamaremos para una entrevista!')
            form.save()
            return redirect("home:index")
    else:
        form = forms.PerroForm()
    context={"form": form}
    return render(request, "home/agregar_perro.html", context)


def agregar_gato(request):
    if request.method == "POST":
        form = forms.GatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home:index")
    else:
        form = forms.GatoForm()
    context={"form": form}
    return render(request, "home/agregar_gato.html", context)


def agregar_exotico(request):
    if request.method == "POST":
        form = forms.ExoticoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home:index")
    else:
        form = forms.ExoticoForm()
    context={"form": form}
    return render(request, "home/agregar_exotico.html", context)