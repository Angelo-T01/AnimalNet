from pyexpat.errors import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
import pandas as pd
from .forms import formulario
from .models import Parametro
from django.contrib.auth.models import User
#from django.contrib import messages


# Create your views here.
def analisis(request):
   return render(request, 'analysis/analisis_base.html')

def mapeo(request):
   return render(request, 'mapeo/mapeo_estaciones.html')


def form(request):
    
    if request.method == 'GET':
        return render(request, 'subirForm.html' ,{
                  'form' : formulario
        })
    else:
        try:
            
            print(request.POST)
            form = formulario(request.POST)
            new_parametros = form.save(commit=False)
            new_parametros.user = request.user
            new_parametros.save()
            print(new_parametros)
            return render(request, 'subirForm.html' ,{
                    'form' : formulario,
                    'success': 'archivo cargado correctamente'
                    })
        except ValueError:
         return render(request, 'subirForm.html' ,{
                  'form' : formulario,
                  'error' : 'datos no validos'
                  })
         
""" def archivo(request,id):
    proyecto = Parametro.objects.get(pk=id)
    print(id)
    return render( request, 'validacion.html',{'proyecto': proyecto})
     """

""" 
def archivo(request):
    if request.method == 'POST':
        form = SubirArchivo(request.POST, request.FILES)
        if form.is_valid():
            archivo = request.FILES['archivo']
            try:
                df = pd.read_excel(archivo)
                # Columnas que deben estar presentes en el archivo Excel y sus respectivos tipos de datos
                columnas_esperadas = {
                    "Idcamara": "texto",
                    "Estacion": "texto",
                    "Lugar": "texto",
                    "Especie": "texto",
                    "Nombre_comun": "texto",
                    "Longitud": "número decimal",
                    "Latitud": "número decimal",
                    "Msnm": "número entero",
                    "Dia": "número entero (menor o igual a 31)",
                    "Mes": "número entero (menor o igual a 12)",
                    "Anyo": "número entero",
                    "Hora": "hora (formato 24:00 hrs)",
                    "Fecha de instalación": "fecha (formato dd/mm/aaaa)",
                    "Fecha de remoción": "fecha (formato dd/mm/aaaa)"
                }

                errores = []

                # Validar que las columnas requeridas estén presentes en el archivo Excel
                columnas_faltantes = [col for col in columnas_esperadas if col not in df.columns]
                if columnas_faltantes:
                    errores.append(f"Las siguientes columnas no están presentes en el archivo Excel: {', '.join(columnas_faltantes)}")

                # Validar cada celda en las columnas requeridas
                for indice, fila in df.iterrows():
                    for columna, tipo in columnas_esperadas.items():
                        if columna not in df.columns:
                            continue
                        
                        valor = fila[columna]
                        if pd.isna(valor):
                            errores.append(f"Fila {indice+2}, Columna {columna}: La celda está vacía")
                            continue
                        
                        if tipo == "texto" and not isinstance(valor, str):
                            errores.append(f"Fila {indice+2}, Columna {columna}: Se esperaba un valor de tipo texto")
                        elif tipo == "número decimal" and not isinstance(valor, float):
                            errores.append(f"Fila {indice+2}, Columna {columna}: Se esperaba un valor de tipo número decimal")
                        elif tipo == "número entero" and not isinstance(valor, int):
                            errores.append(f"Fila {indice+2}, Columna {columna}: Se esperaba un valor de tipo número entero")
                        elif tipo == "número entero (menor o igual a 31)" and (not isinstance(valor, int) or valor > 31):
                            errores.append(f"Fila {indice+2}, Columna {columna}: Valor incorrecto para el día (debe ser un número entero menor o igual a 31)")
                        elif tipo == "número entero (menor o igual a 12)" and (not isinstance(valor, int) or valor > 12):
                            errores.append(f"Fila {indice+2}, Columna {columna}: Valor incorrecto para el mes (debe ser un número entero menor o igual a 12)")
                        elif tipo == "hora (formato 24:00 hrs)":
                            try:
                                pd.to_datetime(valor, format='%H:%M:%S', errors='raise')
                            except ValueError:
                                errores.append(f"Fila {indice+2}, Columna {columna}: Formato de hora incorrecto (se esperaba formato 24:00 hrs)")

                # Validar el formato de las fechas
                for columna in ["Fecha de instalación", "Fecha de remoción"]:
                    if columna in df.columns:
                        try:
                            pd.to_datetime(df[columna], format='%d/%m/%Y', errors='raise')
                        except ValueError:
                            errores.append(f"La columna {columna} tiene un formato de fecha incorrecto (se esperaba formato dd/mm/aaaa)")

                # Mostrar errores
                if errores:
                    for error in errores:
                        return render(request, 'validacion.html', {'form': SubirArchivo,'message': error(request, error)})
                else:
                    messages.success(request, "Todos los datos son válidos")
                    return render(request, 'validacion.html', {'message': "Datos guardados con éxito!" })
            except Exception as e:
                messages.error(request, f"Error al procesar el archivo: {e}")
    else:
        form = SubirArchivo()
    return render(request, 'validacion.html', {'form': SubirArchivo, 'mensaje': "Seleccione un archivo Excel para validar."})

      """