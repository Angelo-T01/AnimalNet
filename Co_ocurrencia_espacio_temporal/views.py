from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def espaciotemp(request):
   return render(request, 'CoocurenciaEspacioTem.html')