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
        if (id > 0):  # Si se envia un id, se obtiene un registro en especifico
            administradores = list(
                Administrador.objects.filter(idadmin=id).values())
            if len(administradores) > 0:
                administrador = administradores[0]
                datitos = {'message': "Operacion exitosa",
                           'administrador': administrador}
            else:
                datitos = {
                    'message': "No existe el administrador o la administradora"}
        else:  # Si no se envia un id, se obtienen todos los registros
            administradores = list(Administrador.objects.values())
            if len(administradores) > 0:
                datitos = {'message': "Operacion exitosa",
                           'administradores': administradores}
            else:
                datitos = {'message': "No hay administradores"}
        return JsonResponse(datitos)

    def post(self, request):
        # Se obtiene el JSON enviado por el cliente
        jd = json.loads(request.body)
        Administrador.objects.create(  # Se crea un nuevo registro en la tabla Administrador
            nombreadmin=jd['nombreadmin'],  # Se obtienen los valores del JSON
            appatadmin=jd['appatadmin'],  # Se obtienen los valores del JSON
            apmatadmin=jd['apmatadmin'],  # Se obtienen los valores del JSON
            contraadmin=jd['contraadmin'],  # Se obtienen los valores del JSON
            correoadmin=jd['correoadmin'],  # Se obtienen los valores del JSON
        )
        datitos = {'message': "Operación exitosa"}
        return JsonResponse(datitos)

    def put(self, request, id):
        # Se obtiene el JSON enviado por el cliente
        jd = json.loads(request.body)
        administradores = list(Administrador.objects.filter(
            idadmin=id).values())  # Se obtiene el registro a modificar
        if len(administradores) > 0:  # Si existe el registro
            administrador = Administrador.objects.get(
                idadmin=id)  # Se obtiene el registro a modificar
            # Se obtienen los valores del JSON
            administrador.nombreadmin = jd['nombreadmin']
            # Se obtienen los valores del JSON
            administrador.appatadmin = jd['appatadmin']
            # Se obtienen los valores del JSON
            administrador.apmatadmin = jd['apmatadmin']
            # Se obtienen los valores del JSON
            administrador.contraadmin = jd['contraadmin']
            # Se obtienen los valores del JSON
            administrador.correoadmin = jd['correoadmin']
            administrador.save()  # Se guardan los cambios
            # Se envia un mensaje de exito
            datitos = {'message': "Operación exitosa"}
        else:
            # Si no existe el registro
            datitos = {
                'message': "No existe el administrador o la administradora"}
        return JsonResponse(datitos)  # Se envia la respuesta al cliente

    def delete(self, request, id):
        administradores = list(Administrador.objects.filter(
            idadmin=id).values())  # Se obtiene el registro a eliminar
        if len(administradores) > 0:  # Si existe el registro
            Administrador.objects.filter(
                idadmin=id).delete()  # Se elimina el registro
            # Se envia un mensaje de exito
            datitos = {'message': "Operación exitosa"}
        else:  # Si no existe el registro
            # Se envia un mensaje de error
            datitos = {
                'message': "No existe el administrador o la administradora"}
        return JsonResponse(datitos)  # Se envia la respuesta al cliente


class CatalogozonasView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):  # Si se envia un id, se obtiene un registro en especifico
            zonas = list(Catalogozonas.objects.filter(idzona=id).values())
            if len(zonas) > 0:
                zona = zonas[0]
                datitos = {'message': "Operacion exitosa", 'zona': zona}
            else:
                datitos = {'message': "No existe la zona"}
        else:  # Si no se envia un id, se obtienen todos los registros
            zonas = list(Catalogozonas.objects.values())
            if len(zonas) > 0:
                datitos = {'message': "Operacion exitosa", 'zonas': zonas}
            else:
                datitos = {'message': "No hay zonas"}
        return JsonResponse(datitos)

    def post(self, request):
        jd = json.loads(request.body)
        Catalogozonas.objects.create(
            colonia=jd['colonia'],
            codigopostal=jd['codigopostal'],
        )
        datitos = {'message': "Operación exitosa"}
        return JsonResponse(datitos)

    def put(self, request, id):
        # Se obtiene el JSON enviado por el cliente
        jd = json.loads(request.body)
        # Se obtiene el registro a modificar
        zonas = list(Catalogozonas.objects.filter(idzona=id).values())
        if len(zonas) > 0:  # Si existe el registro
            # Se obtiene el registro a modificar
            zonas = Catalogozonas.objects.get(idzona=id)
            zonas.colonia = jd['colonia']  # Se obtienen los valores del JSON
            # Se obtienen los valores del JSON
            zonas.codigopostal = jd['codigopostal']
            # Se envia un mensaje de exito
            datitos = {'message': "Operación exitosa"}
        else:
            # Si no existe el registro
            datitos = {'message': "No existe la zona"}
        return JsonResponse(datitos)  # Se envia la respuesta al cliente

    def delete(self, request, id):
        # Se obtiene el registro a eliminar
        zonas = list(Catalogozonas.objects.filter(idzona=id).values())
        if len(zonas) > 0:  # Si existe el registro
            Catalogozonas.objects.filter(
                idzona=id).delete()  # Se elimina el registro
            # Se envia un mensaje de exito
            datitos = {'message': "Operación exitosa"}
        else:  # Si no existe el registro
            # Se envia un mensaje de error
            datitos = {'message': "No existe la zona"}
        return JsonResponse(datitos)  # Se envia la respuesta al cliente


class ClienteView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):  # Si se envia un id, se obtiene un registro en especifico
            clientes = list(Cliente.objects.filter(idcliente=id).values())
            if len(clientes) > 0:
                cliente = clientes[0]
                datitos = {'message': "Operacion exitosa", 'cliente': cliente}
            else:
                datitos = {'message': "No existe el cliente"}
        else:  # Si no se envia un id, se obtienen todos los registros
            clientes = list(Cliente.objects.values())
            if len(clientes) > 0:
                datitos = {'message': "Operacion exitosa",
                           'clientes': clientes}
            else:
                datitos = {'message': "No hay clientes"}
        return JsonResponse(datitos)

    def post(self, request):
        jd = json.loads(request.body)
        Cliente.objects.create(
            nombrecliente=jd['nombrecliente'],
            appatcliente=jd['appatcliente'],
            apmatcliente=jd['apmatcliente'],
            contracliente=jd['contracliente'],
            correocliente=jd['correocliente'],
            callecliente=jd['callecliente'],
            colcliente=jd['colcliente'],
            numextcliente=jd['numextcliente'],
            cpcliente=jd['cpcliente'],
        )
        datitos = {'message': "Operación exitosa"}
        return JsonResponse(datitos)

    def put(self, request, id):
        # Se obtiene el JSON enviado por el cliente
        jd = json.loads(request.body)
        # Se obtiene el registro a modificar
        clientes = list(Cliente.objects.filter(idcliente=id).values())
        if len(clientes) > 0:  # Si existe el registro
            # Se obtiene el registro a modificar
            clientes = Cliente.objects.get(idcliente=id)
            # Se obtienen los valores del JSON
            clientes.nombrecliente = jd['nombrecliente']
            # Se obtienen los valores del JSON
            clientes.appatcliente = jd['appatcliente']
            # Se obtienen los valores del JSON
            clientes.apmatcliente = jd['apmatcliente']
            # Se obtienen los valores del JSON
            clientes.contracliente = jd['contracliente']
            # Se obtienen los valores del JSON
            clientes.correocliente = jd['correocliente']
            # Se obtienen los valores del JSON
            clientes.callecliente = jd['callecliente']
            # Se obtienen los valores del JSON
            clientes.colcliente = jd['colcliente']
            # Se obtienen los valores del JSON
            clientes.numextcliente = jd['numextcliente']
            # Se obtienen los valores del JSON
            clientes.cpcliente = jd['cpcliente']
            # Se envia un mensaje de exito
            datitos = {'message': "Operación exitosa"}
        else:
            # Si no existe el registro
            datitos = {'message': "No existe el o la cliente"}
        return JsonResponse(datitos)  # Se envia la respuesta al cliente

    def delete(self, request, id):
        # Se obtiene el registro a eliminar
        clientes = list(Cliente.objects.filter(idcliente=id).values())
        if len(clientes) > 0:  # Si existe el registro
            # Se elimina el registro
            Cliente.objects.filter(idcliente=id).delete()
            # Se envia un mensaje de exito
            datitos = {'message': "Operación exitosa"}
        else:  # Si no existe el registro
            # Se envia un mensaje de error
            datitos = {'message': "No existe el o la cliente"}
        return JsonResponse(datitos)  # Se envia la respuesta al cliente


class ReportefallasView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):  # Si se envia un id, se obtiene un registro en especifico
            reportes = list(Reportefallas.objects.filter(
                idfalla=id).values())
            if len(reportes) > 0:
                reporte = reportes[0]
                datitos = {'message': "Operacion exitosa", 'reporte': reporte}
            else:
                datitos = {'message': "No existe el reporte"}
        else:  # Si no se envia un id, se obtienen todos los registros
            reportes = list(Reportefallas.objects.values())
            if len(reportes) > 0:
                datitos = {'message': "Operacion exitosa",
                           'reportes': reportes}
            else:
                datitos = {'message': "No hay reportes"}
        return JsonResponse(datitos)

    def post(self, request):
        jd = json.loads(request.body)
        Reportefallas.objects.create(
            motivorep=jd['motivorep'], # Se obtienen los valores del JSON
            fecharep=jd['fecharep'], # Se obtienen los valores del JSON
            estatusrep=jd['estatusrep'], # Se obtienen los valores del JSON
            clavecliente=jd['clavecliente'] # Se obtienen los valores del JSON
        )
        datitos = {'message': "Operación exitosa"}
        return JsonResponse(datitos)

    def put(self, request, id):
        # Se obtiene el JSON enviado por el cliente
        jd = json.loads(request.body)
        # Se obtiene el registro a modificar
        reportes = list(Reportefallas.objects.filter(idfalla=id).values())
        if len(reportes) > 0:  # Si existe el registro
            # Se obtiene el registro a modificar
            reportes = Reportefallas.objects.get(idfalla=id)
            # Se obtienen los valores del JSON
            reportes.motivorep = jd['motivorep']
            # Se obtienen los valores del JSON
            reportes.fecharep = jd['fecharep']
            # Se obtienen los valores del JSON
            reportes.estatusrep = jd['estatusrep']
            # Se obtienen los valores del JSON
            reportes.clavecliente = jd['clavecliente']
            # Se envia un mensaje de exito
            datitos = {'message': "Operación exitosa"}
        else:
            # Si no existe el registro
            datitos = {'message': "No existe el reporte"}
        return JsonResponse(datitos)  # Se envia la respuesta al cliente

    def delete(self, request, id):
        # Se obtiene el registro a eliminar
        reportes = list(Reportefallas.objects.filter(idfalla=id).values())
        if len(reportes) > 0:  # Si existe el registro
            Reportefallas.objects.filter(
                idfalla=id).delete()  # Se elimina el registro
            # Se envia un mensaje de exito
            datitos = {'message': "Operación exitosa"}
        else:  # Si no existe el registro
            # Se envia un mensaje de error
            datitos = {'message': "No existe el reporte"}
        return JsonResponse(datitos)  # Se envia la respuesta al cliente
