from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required
from .forms import CustomUserForm,ReservaForm
from .models import Reserva
# Create your views here.
def home(request):
    return render(request, "core/home.html")

def eventos(request):
    return render(request, "core/eventos.html")


def lista(request):
    reservas = Reserva.objects.all()
    data = {
        'reserva':reservas
    }
    return render(request, "core/lista.html",data)


def reserva(request):
    data= {
        'form': ReservaForm()
    }
    if request.method == 'POST':
        formulario = ReservaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje']="Guardado Correctamente"

    return render(request,'core/reserva.html',data)

def modreserva(request, id):
    reservas = Reserva.objects.get(id=id)
    data = {
        'form': ReservaForm(instance=reservas)
    }

    if request.method == 'POST':
        formulario = ReservaForm(data=request.POST, instance=reservas, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado correctamente"
        data['form'] = ReservaForm(instance=Reserva.objects.get(id=id))

    return render(request, 'core/modreserva.html', data)


def eliminar_reserva(request, id):
    reservas = Reserva.objects.get(id=id)
    reservas.delete()

    return redirect(to="lista")
def galeria(request):
    return render(request, "core/galeria.html")

def info(request):
    return render(request, "core/info.html")

def contacto(request):
    return render(request, "core/contacto.html")

def carta(request):
    return render(request, "core/carta.html")
def Registro_usuario(request):
    data= {
        'form': CustomUserForm()
    }
    
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        formulario = CustomUserForm(request.POST)
        # Si el formulario es válido...
        if formulario.is_valid():

            # Creamos la nueva cuenta de usuario
            formulario.save()
            #redirigir si esta autenticado
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect(to='/')

           
    return render(request,'registration/registrar.html',data)   
    



def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')
#CRUD POP SUSHI
