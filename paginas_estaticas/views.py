from django.shortcuts import render , redirect
from django.http import HttpResponse

# Create your views here.
def home(request):
   return render(request, 'pages/home.html')
def cactaristicas(request):
    return render( request, 'pages/caracteristicas.html')
def colaboladores(request):
    return render( request, 'pages/colaboladores.html')
def guia(request):
    return render( request, 'pages/Guia_de_uso.html')
def ref(request):
    return render( request, 'pages/referencias.html')
def dicc(request):
    return render( request, 'pages/diccionario_de_datos.html')
def politica(request):
    return render( request, 'pages/politica_de_uso.html')
def analisis(request):
   return render(request, 'pages/analisis_base.html')

