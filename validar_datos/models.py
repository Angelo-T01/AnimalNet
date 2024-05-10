from django.db import models
from django.contrib.auth.models import User

class Parametro(models.Model):
    
    NombreProyecto = models.CharField(max_length=200)
    NumEspecies = models.PositiveIntegerField()
    NumEstaciones = models.PositiveIntegerField() 
    EstudioInicio = models.DateTimeField(null=True)
    EstudioFin = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ConjuntoDatos = models.BinaryField(null=True) 
    CamarasInfo = models.BinaryField(null=True)
   
   

class Task(models.Model):
    title = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    