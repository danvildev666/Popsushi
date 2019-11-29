from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime
from .models import Galeriap,Carrusel,Reserva,Menu,Sucursal


class CustomUserForm(UserCreationForm):
    pass
class ReservaForm(ModelForm):

    
    class Meta:
        model = Reserva
        fields  = ['nombre', 'rut', 'menu', 'sucursal', 'asistentes','fecha_reserva','tipo']

        widgets = {
            'fecha_reserva ':forms.SelectDateWidget(years=range(2019, 2030))
            
        }
    
    def clean_fecha_reserva (self):
        fecha = self.cleaned_data['fecha_reserva']

        if fecha < datetime.date.today():
            raise forms.ValidationError("La fecha no puede ser menor al día de hoy")

        return fecha
        