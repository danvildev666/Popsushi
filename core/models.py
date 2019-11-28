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

class Menu(models.Model):
    #id -> numero autoincrementable
    nombre = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=80)
    valor  = models.IntegerField()

    def __str__(self):
        return self.nombre

class Sucursal(models.Model):
    #id -> numero autoincrementable
    nombre = models.CharField(max_length=80)
    direccion = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre 

class Tipo(models.Model):
    #id -> numero autoincrementable
    nombre = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=80)
    costo  = models.IntegerField()


    def __str__(self):
        return self.nombre 

class Reserva(models.Model):
    nombre = models.CharField(max_length=200)
    rut = models.CharField(max_length=200)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    asistentes  = models.IntegerField()
    fecha_reserva = models.DateField()
    
    
    def __str__(self):
        return self.nombre