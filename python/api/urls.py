from django.urls import path
from .views import *

urlpatterns = { # Se establecen los endpoints o URL de la API para obtener información de la base de datos a través de los metodos GET, POST, PUT y DELETE
    # Endpoints generales de la API
    path('administradores/', AdministradorView.as_view(), name='lista_administradores'),
    path('zonas/', CatalogozonasView.as_view(), name='lista_zonas'),
    path('clientes/', ClienteView.as_view(), name='lista_clientes'),
    path('reportes/', ReportefallasView.as_view(), name='lista_reportes'),
    # Endpoints especificos de la API, se usa el id para obtener un registro en especifico
    path('administradores/<int:id>', AdministradorView.as_view(), name='proceso_administradores'),
    path('zonas/<int:id>', CatalogozonasView.as_view(), name='proceso_zonas'),
    path('clientes/<int:id>', ClienteView.as_view(), name='proceso_clientes'),
    path('reportes/<int:id>', ReportefallasView.as_view(), name='proceso_reportes')
}