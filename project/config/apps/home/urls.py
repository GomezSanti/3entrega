from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index, name="index"),
    path("agregar_perro/", views.agregar_perro, name="agregar_perro"),
    path("agregar_gato/", views.agregar_gato, name="agregar_gato"),
    path("agregar_exotico/", views.agregar_exotico, name="agregar_exotico"),
    path("login/", LoginView.as_view(template_name="home/login.html"), name="login"),
    path("registro/", views.registro, name = "registro"),
    path("logout/", views.logout_request, name="logout"),
    path("about/", views.about_view, name="about"),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)