from typing import Any
from django import http
from django.views import View
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

# Create your views here.
class AdministradorView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id>0): # Si se envia un id, se obtiene un registro en especifico
            administradores = list(Administrador.objects.filter(idadmin=id).values())
            if len(administradores) > 0:
                administrador = administradores[0]
                datitos = {'message': "Operacion exitosa", 'administrador': administrador}
            else:
                datitos = {'message': "No existe el administrador o la administradora"}
        else: # Si no se envia un id, se obtienen todos los registros
            administradores = list(Administrador.objects.values())
            if len(administradores) > 0:
                datitos = {'message': "Operacion exitosa", 'administradores': administradores}
            else:
                datitos = {'message': "No hay administradores"}
        return JsonResponse(datitos)

    def post(self, request):
        jd = json.loads(request.body) # Se obtiene el JSON enviado por el cliente
        Administrador.objects.create( # Se crea un nuevo registro en la tabla Administrador
            nombreadmin = jd['nombreadmin'], # Se obtienen los valores del JSON
            appatadmin = jd['appatadmin'], # Se obtienen los valores del JSON
            apmatadmin = jd['apmatadmin'], # Se obtienen los valores del JSON
            contraadmin = jd['contraadmin'], # Se obtienen los valores del JSON
            correoadmin = jd['correoadmin'], # Se obtienen los valores del JSON
        )
        datitos = {'message': "Operación exitosa"}
        return JsonResponse(datitos)
    
    def put(self, request, id):
        jd = json.loads(request.body) # Se obtiene el JSON enviado por el cliente
        administradores = list(Administrador.objects.filter(idadmin=id).values()) # Se obtiene el registro a modificar
        if len(administradores) > 0: #Si existe el registro
            administrador = Administrador.objects.get(idadmin=id) # Se obtiene el registro a modificar
            administrador.nombreadmin = jd['nombreadmin'] # Se obtienen los valores del JSON
            administrador.appatadmin = jd['appatadmin'] # Se obtienen los valores del JSON
            administrador.apmatadmin = jd['apmatadmin'] # Se obtienen los valores del JSON
            administrador.contraadmin = jd['contraadmin'] # Se obtienen los valores del JSON
            administrador.correoadmin = jd['correoadmin'] # Se obtienen los valores del JSON
            administrador.save() # Se guardan los cambios
            datitos = {'message': "Operación exitosa"} # Se envia un mensaje de exito
        else:
            datitos = {'message': "No existe el administrador o la administradora"} # Si no existe el registro
        return JsonResponse(datitos) # Se envia la respuesta al cliente
    
    def delete(self, request, id):
        administradores = list(Administrador.objects.filter(idadmin=id).values()) # Se obtiene el registro a eliminar
        if len(administradores) > 0: # Si existe el registro
            Administrador.objects.filter(idadmin=id).delete() # Se elimina el registro
            datitos = {'message': "Operación exitosa"} # Se envia un mensaje de exito
        else: # Si no existe el registro
            datitos = {'message': "No existe el administrador o la administradora"} # Se envia un mensaje de error
        return JsonResponse(datitos) # Se envia la respuesta al cliente

class CatalogozonasView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request, id=0):
        if (id>0): # Si se envia un id, se obtiene un registro en especifico
            zonas = list(Catalogozonas.objects.filter(idzona=id).values())
            if len(zonas) > 0:
                zona = zonas[0]
                datitos = {'message': "Operacion exitosa", 'zona': zona}
            else:
                datitos = {'message': "No existe la zona"}
        else: # Si no se envia un id, se obtienen todos los registros
            zonas = list(Catalogozonas.objects.values())
            if len(zonas) > 0:
                datitos = {'message': "Operacion exitosa", 'zonas': zonas}
            else:
                datitos = {'message': "No hay zonas"}
        return JsonResponse(datitos)

    def post(self, request):
        jd = json.loads(request.body)
        Catalogozonas.objects.create(
            nombrezona = jd['nombrezona'],
            descripcionzona = jd['descripcionzona'],
            imagen = jd['imagen'],
        )
        datitos = {'message': "Operación exitosa"}
        return JsonResponse(datitos)
    
    def put(self, request, id):
        jd = json.loads(request.body) # Se obtiene el JSON enviado por el cliente
        zonas = list(Catalogozonas.objects.filter(idzonas=id).values()) # Se obtiene el registro a modificar
        if len(zonas) > 0: #Si existe el registro
            zonas = Catalogozonas.objects.get(idzonas=id) # Se obtiene el registro a modificar
            zonas.colonia = jd['colonia'] # Se obtienen los valores del JSON
            zonas.codigopostal = jd['codigopostal'] # Se obtienen los valores del JSON
            datitos = {'message': "Operación exitosa"} # Se envia un mensaje de exito
        else:
            datitos = {'message': "No existe la zona"} # Si no existe el registro
        return JsonResponse(datitos) # Se envia la respuesta al cliente
    
    def delete(self, request, id):
        zonas = list(Catalogozonas.objects.filter(idzonas=id).values()) # Se obtiene el registro a eliminar
        if len(zonas) > 0: # Si existe el registro
            Catalogozonas.objects.filter(idzonas=id).delete() # Se elimina el registro
            datitos = {'message': "Operación exitosa"} # Se envia un mensaje de exito
        else: # Si no existe el registro
            datitos = {'message': "No existe la zona"} # Se envia un mensaje de error
        return JsonResponse(datitos) # Se envia la respuesta al cliente

class ClienteView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request, id=0):
        if (id>0): # Si se envia un id, se obtiene un registro en especifico
            clientes = list(Cliente.objects.filter(idcliente=id).values())
            if len(clientes) > 0:
                cliente = clientes[0]
                datitos = {'message': "Operacion exitosa", 'cliente': cliente}
            else:
                datitos = {'message': "No existe el cliente"}
        else: # Si no se envia un id, se obtienen todos los registros
            clientes = list(Cliente.objects.values())
            if len(clientes) > 0:
                datitos = {'message': "Operacion exitosa", 'clientes': clientes}
            else:
                datitos = {'message': "No hay clientes"}
        return JsonResponse(datitos)

    def post(self, request):
        jd = json.loads(request.body)
        Cliente.objects.create(
            nombrecliente = jd['nombrecliente'],
            appatcliente = jd['appatcliente'],
            apmatcliente = jd['apmatcliente'],
            contracliente = jd['contracliente'],
            correocliente = jd['correocliente'],
            callecliente = jd['callecliente'],
            colcliente = jd['colcliente'],
            numextcliente = jd['numextcliente'],
            cpcliente = jd['cpcliente'],
        )
        datitos = {'message': "Operación exitosa"}
        return JsonResponse(datitos)
    
    def put(self, request, id):
        jd = json.loads(request.body) # Se obtiene el JSON enviado por el cliente
        clientes = list(Cliente.objects.filter(idcliente=id).values()) # Se obtiene el registro a modificar
        if len(clientes) > 0: #Si existe el registro
            clientes = Cliente.objects.get(idcliente=id) # Se obtiene el registro a modificar
            clientes.nombrecliente = jd['nombrecliente'] # Se obtienen los valores del JSON
            clientes.appatcliente = jd['appatcliente'] # Se obtienen los valores del JSON
            clientes.apmatcliente = jd['apmatcliente'] # Se obtienen los valores del JSON
            clientes.contracliente = jd['contracliente'] # Se obtienen los valores del JSON
            clientes.correocliente = jd['correocliente'] # Se obtienen los valores del JSON
            clientes.callecliente = jd['callecliente'] # Se obtienen los valores del JSON
            clientes.colcliente = jd['colcliente'] # Se obtienen los valores del JSON
            clientes.numextcliente = jd['numextcliente'] # Se obtienen los valores del JSON
            clientes.cpcliente = jd['cpcliente'] # Se obtienen los valores del JSON
            datitos = {'message': "Operación exitosa"} # Se envia un mensaje de exito
        else:
            datitos = {'message': "No existe el o la cliente"} # Si no existe el registro
        return JsonResponse(datitos) # Se envia la respuesta al cliente
    
    def delete(self, request, id):
        clientes = list(Cliente.objects.filter(idcliente=id).values()) # Se obtiene el registro a eliminar
        if len(clientes) > 0: # Si existe el registro
            Cliente.objects.filter(idcliente=id).delete() # Se elimina el registro
            datitos = {'message': "Operación exitosa"} # Se envia un mensaje de exito
        else: # Si no existe el registro
            datitos = {'message': "No existe el o la cliente"} # Se envia un mensaje de error
        return JsonResponse(datitos) # Se envia la respuesta al cliente

class ReportefallasView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request, id=0):
        if (id>0): # Si se envia un id, se obtiene un registro en especifico
            reportes = list(Reportefallas.objects.filter(idreporte=id).values())
            if len(reportes) > 0:
                reporte = reportes[0]
                datitos = {'message': "Operacion exitosa", 'reporte': reporte}
            else:
                datitos = {'message': "No existe el reporte"}
        else: # Si no se envia un id, se obtienen todos los registros
            reportes = list(Reportefallas.objects.values())
            if len(reportes) > 0:
                datitos = {'message': "Operacion exitosa", 'reportes': reportes}
            else:
                datitos = {'message': "No hay reportes"}
        return JsonResponse(datitos)

    def post(self, request):
        jd = json.loads(request.body)
        Reportefallas.objects.create(
            idcliente = jd['idcliente'],
            idzona = jd['idzona'],
            descripcionfalla = jd['descripcionfalla'],
            imagenfalla = jd['imagenfalla'],
        )
        datitos = {'message': "Operación exitosa"}
        return JsonResponse(datitos)
    
    def put(self, request, id):
        jd = json.loads(request.body) # Se obtiene el JSON enviado por el cliente
        reportes = list(Reportefallas.objects.filter(idreporte=id).values()) # Se obtiene el registro a modificar
        if len(reportes) > 0: #Si existe el registro
            reportes = Reportefallas.objects.get(idreporte=id) # Se obtiene el registro a modificar
            reportes.motivorep  = jd['motivorep'] # Se obtienen los valores del JSON
            reportes.fecharep = jd['fecharep'] # Se obtienen los valores del JSON
            reportes.estatusrep = jd['estatusrep'] # Se obtienen los valores del JSON
            reportes.clavecliente = jd['clavecliente'] # Se obtienen los valores del JSON
            datitos = {'message': "Operación exitosa"} # Se envia un mensaje de exito
        else:
            datitos = {'message': "No existe el reporte"} # Si no existe el registro
        return JsonResponse(datitos) # Se envia la respuesta al cliente
    
    def delete(self, request, id):
        reportes = list(Reportefallas.objects.filter(idreportes=id).values()) # Se obtiene el registro a eliminar
        if len(reportes) > 0: # Si existe el registro
            Reportefallas.objects.filter(idreportes=id).delete() # Se elimina el registro
            datitos = {'message': "Operación exitosa"} # Se envia un mensaje de exito
        else: # Si no existe el registro
            datitos = {'message': "No existe el reporte"} # Se envia un mensaje de error
        return JsonResponse(datitos) # Se envia la respuesta al cliente