from django.urls import path
from django.contrib import admin
from .views import home,login,logout,register,Registro_usuario,eventos,galeria,info,contacto,carta
from core import views
urlpatterns = [
    path('',home, name='home'),
    path('carta/',carta, name='carta'),
    path('eventos/',eventos, name='eventos'),
    path('galeria/',galeria, name='galeria'),
    path('info/',info, name='info'),
    path('contacto/',contacto, name='contacto'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('logout/', logout, name='logout'),
    path('registro/', Registro_usuario, name='registro_usuario'),
  
   
]
