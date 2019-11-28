import os
from django.db import models
from django.conf import settings
from django.utils.safestring import mark_safe


class Carrusel (models.Model):
   
    descripcion = models.CharField(max_length=30)
    foto = models.ImageField(upload_to='Photos', null=True, blank=True)
    def __str__(self):
        return self.descripcion

class Galeriap(models.Model):
    #id -> numero autoincrementable
    imagen = models.ImageField(null=True, blank=True)
    descripcion = models.CharField(max_length=30)
    def __str__(self):
        return self.descripcion

    

