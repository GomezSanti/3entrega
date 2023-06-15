from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Perro(models.Model):
    nombre = models.CharField(max_length=100)
    años = models.IntegerField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    raza = models.CharField(max_length=100)
    teléfono=models.IntegerField()

    def __str__(self):
        return self.raza  

class Gato(models.Model):
    nombre = models.CharField(max_length=100)
    años = models.IntegerField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    raza = models.CharField(max_length=100)
    teléfono=models.IntegerField()

    def __str__(self):
        return self.raza  
    
class Exotico(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    años = models.IntegerField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    teléfono=models.IntegerField()

    def __str__(self):
        return self.especie
    
class Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    teléfono = models.IntegerField()
    avatar = models.ImageField(upload_to="avatars", blank=True, null=True)

    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"

    def __str__(self):
        return f"{self.usuario.username}"