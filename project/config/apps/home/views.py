from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import views as auth_views
from django.db import models
from .forms import UserRegisterForm



def index(request):
    avatar_url = None
    if request.user.is_authenticated:
        usuario = request.user.usuario
        if usuario.avatar:
            avatar_url = usuario.avatar.url
    return render(request, "home/index.html", {"user": request.user, "avatar_url": avatar_url})


#Formulario de perros
def agregar_perro(request):
    if request.method == "POST":
        form = forms.PerroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ya contamos con los datos de nuestro amiguit@. ¡Pronto te llamaremos para una entrevista!')
            return redirect("home:index")
    else:
        form = forms.PerroForm()
    context = {"form": form}
    return render(request, "home/agregar_perro.html", context)

# Formulario para gatos
def agregar_gato(request):
    if request.method == "POST":
        form = forms.GatoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ya contamos con los datos de nuestro amiguit@. ¡Pronto te llamaremos para una entrevista!')
            return redirect("home:index")
    else:
        form = forms.GatoForm()
    context = {"form": form}
    return render(request, "home/agregar_gato.html", context)

# Formulario para animales exóticos
def agregar_exotico(request):
    if request.method == "POST":
        form = forms.ExoticoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ya contamos con los datos de nuestro amiguit@. ¡Pronto te llamaremos para una entrevista!')
            return redirect("home:index")
    else:
        form = forms.ExoticoForm()
    context = {"form": form}
    return render(request, "home/agregar_exotico.html", context)


#Logeo de usuarios
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)

                return render(request, "home/index.html", {"mensaje": f"Bienvenido amigo {usuario}"})
            else:
                return render(request, "home/index.html", {"mensaje": "Error, usuario o contraseña incorrectos"})
        else:
            return render(request, "home/index.html", {"mensaje": "Error, formulario erróneo"})

    form = AuthenticationForm()

    return render(request, "home/login.html", {"form": form})


#Registrar usuarios en mi web

def registro(request):
    if request.method =="POST":
        
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "home/index.html", {"mensaje":"Usuario creado exitosamente"})


    else:
        form = UserRegisterForm()

    return render (request,"home/registro.html", {"form":form})

def logout_request(request):
    logout(request)
    return render(request, "home/index.html", {"mensaje":"La sesión ha finalizado"})


def about_view(request):
    return render(request, "home/about.html")

