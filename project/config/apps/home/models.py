from django.db import models

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
    
