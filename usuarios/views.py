from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.

# LOGIN  Y ERRORES
def signup(request):

    if request.method == 'GET':
        return render(request, 'registration/signup.html',{
         'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('analisis')
                # return HttpResponse('Usuario creado exitosamente')
            except:
                 return render(request, 'registration/signup.html', {
                    'form': UserCreationForm,
                    "error":"El usuario ya existe"
                })
        return render(request, 'registration/signup.html', {
                'form': UserCreationForm,
                "error":"las contraseñas no coinciden"
                })

#cerrar sesion
def cerar_sesion(request):
   logout(request)
   return redirect('home')

def signin (request):
    if request.method == 'GET':
        return render(request,'registration/signin.html',{
            'form': AuthenticationForm
        })
    else:
        user= authenticate(
            request, username=request.POST['username'], password=request.POST
            ['password'])
        if user is None:
            return render(request,'registration/signin.html',{
                'form': AuthenticationForm,
                'error': 'Usuario o cantraseña incorrecta'
            })
        else:
            login(request, user)
            return redirect('analisis')
   