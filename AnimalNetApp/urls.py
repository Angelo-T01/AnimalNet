from django.contrib import admin
from django.urls import path 
from usuarios import views as usuarios_views 
from paginas_estaticas import views as paginas_estaticas_views
from validar_datos import views as validar_datos_views
from Co_ocurrencia_espacio_temporal import views as EspacioTemp_views


urlpatterns = [
        path('admin/', admin.site.urls),
        
        #Pagina wevb
        path('',paginas_estaticas_views.home , name='home'),
        path('colaboladores/', paginas_estaticas_views.colaboladores , name='colaboladores'),
        path('ref/', paginas_estaticas_views.ref , name='ref'),
        path('caracteristicas/', paginas_estaticas_views.cactaristicas , name='caracteristicas'),
        path('guia/', paginas_estaticas_views.guia , name='guia'),
        path('dicc/', paginas_estaticas_views.dicc , name='dicc'),    
        path('politica/', paginas_estaticas_views.politica , name='politica'),    
        path('analisis/', paginas_estaticas_views.analisis , name='analisis'),    
       
       
       #registro de usuarios
        path('signup/', usuarios_views.signup , name='signup'),
        path('logout/', usuarios_views.cerar_sesion , name='logout'),
        path('signin/', usuarios_views.signin , name='signin'),
        
    ]