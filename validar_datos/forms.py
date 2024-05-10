from django.forms import ModelForm
from .models import Parametro
from django import forms

class formulario(ModelForm):
    class Meta:
       model = Parametro
       fields = ['NombreProyecto','NumEspecies','NumEstaciones','EstudioInicio','EstudioFin']
