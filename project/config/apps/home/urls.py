from django.urls import path

from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("agregar_perro/", views.agregar_perro, name="agregar_perro"),
    path("agregar_gato/", views.agregar_gato, name="agregar_gato"),
    path("agregar_exotico/", views.agregar_exotico, name="agregar_exotico"),
]