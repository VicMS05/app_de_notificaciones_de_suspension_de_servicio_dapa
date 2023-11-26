from django.urls import path
from .views import AdministradorView, CatalogozonasView, ClienteView, ReportefallasView

urlpatterns = {  # Se establecen los endpoints o URL de la API para obtener información de la base de datos a través de los metodos GET, POST, PUT y DELETE
    # Endpoints generales de la API
    # select * from administradores
    path('administradores/', AdministradorView.as_view(),
         name='lista_administradores'),
    # select * from catalogozonas
    path('zonas/', CatalogozonasView.as_view(), name='lista_zonas'),
    # select * from clientes
    path('clientes/', ClienteView.as_view(), name='lista_clientes'),
    # select * from reportefallas
    path('reportes/', ReportefallasView.as_view(), name='lista_reportes'),
    # Endpoints especificos de la API, se usa el id o correo para obtener un registro en especifico
    # select * from administradores where correoadmin = correo
    path('administradores/<str:correo>', AdministradorView.as_view(),
        name='proceso_administradores'),
    # select * from catalogozonas where idzona = id
    path('zona/<int:id>', CatalogozonasView.as_view(), name='proceso_zonas'),
    # select * from clientes where idcliente = id
    path('cliente_id/<int:id>', ClienteView.as_view(), name='proceso_clientes_id'),
    # select * from clientes where correocliente = correo
    path('cliente_correo/<str:correo>', ClienteView.as_view(),
        name='proceso_clientes_correo'),
    # select * from reportefallas where idreporte = id
    path('reporte/<int:id>', ReportefallasView.as_view(), name='proceso_reportes')
}
