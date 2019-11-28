from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required
from .forms import CustomUserForm
# Create your views here.
def home(request):
    return render(request, "core/home.html")

def eventos(request):
    return render(request, "core/eventos.html")

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
    


def register(request):
    # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente 
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')
    # Si queremos borramos los campos de ayuda
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None
    # Si llegamos al final renderizamos el formulario
    return render(request, "core/register.html", {'form': form})
   


def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')
#CRUD POP SUSHI
