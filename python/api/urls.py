from django.urls import path
from .views import *

urlpatterns = {
    path('administrador/', AdministradorView.as_view(), name='lista_administradores'),
}