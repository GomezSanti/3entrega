from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("agregar_perro/", views.agregar_perro, name="agregar_perro"),
    path("agregar_gato/", views.agregar_gato, name="agregar_gato"),
    path("agregar_exotico/", views.agregar_exotico, name="agregar_exotico"),
    path("login/", views.login_request, name="login"),
    path("registro/", views.registro, name = "registro"),
    path("logout/", views.logout_request, name="logout"),
]