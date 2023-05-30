from django.urls import path

from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("agregar-perro/", views.agregar_perro, name="agregar-perro"),
    path("agregar-gato/", views.agregar_gato, name="agregar-gato"),
    path("agregar-exotico/", views.agregar_exotico, name="agregar-exotico"),
]