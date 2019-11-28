from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime
from .models import Galeriap,Carrusel


class CustomUserForm(UserCreationForm):
    pass
class GaleriaForm(ModelForm):

    nombre = forms.CharField(min_length=2, max_length=200)
    duracion = forms.IntegerField(min_value=5, max_value=500)
    class Meta:
        model = Galeriap
        fields  = ['descripcion', 'imagen']

        