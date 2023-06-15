from django.contrib import admin

from . import models


admin.site.register(models.Perro)
admin.site.register(models.Gato)
admin.site.register(models.Exotico)
admin.site.register(models.Usuario)

