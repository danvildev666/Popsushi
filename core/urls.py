from django.urls import path
from django.contrib import admin
from .views import home,login,logout,Registro_usuario,eventos,galeria,info,contacto,carta,reserva
from core import views
urlpatterns = [
    path('',home, name='home'),
    path('reserva/',reserva, name='reserva'),
    path('carta/',carta, name='carta'),
    path('eventos/',eventos, name='eventos'),
    path('galeria/',galeria, name='galeria'),
    path('info/',info, name='info'),
    path('contacto/',contacto, name='contacto'),
    
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('logout/', logout, name='logout'),
    path('registro/', Registro_usuario, name='registro_usuario'),
  
   
]
