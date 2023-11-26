import json
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.exceptions import ObjectDoesNotExist
from .models import Administrador, Catalogozonas, Cliente, Reportefallas

# Create your views here.


class AdministradorView(View):
    """"Esta clase es una vista para el modelo o entidad 
    Administrador donde se establecen los métodos HTTP (GET, POST, PUT, DELETE)"""

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        # Se desactiva el CSRF para poder hacer peticiones desde el cliente
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, correo=""):
        """Metodo GET para realizar consultas de la tabla Administrador"""
        if correo != "":  # Si se envia un correo, se obtiene un registro en especifico
            # select * from administrador where correoadmin = correo
            administradores = list(
                Administrador.objects.filter(correoadmin=correo).values())
            if len(administradores) > 0:  # Si existe el registro
                administrador = administradores[0]
                datitos = {'message': "Operacion exitosa",
                            'administrador': administrador}
            else:  # Si no existe el registro
                datitos = {
                    'message': "No existe el administrador o la administradora"}
        else:  # Si no se envia un correo, se obtienen todos los registros
            # select * from administrador
            administradores = list(Administrador.objects.values())
            if len(administradores) > 0:  # Si existe el registro
                datitos = {'message': "Operacion exitosa",
                            'administradores': administradores}
            else:  # Si no existe el registro
                datitos = {'message': "No hay administradores"}
        # Se envia la respuesta al cliente en formato JSON
        return JsonResponse(datitos)

    def post(self, request):
        """Método POST para insertar un registro en la tabla Administrador"""
        # Se obtiene el JSON enviado por el cliente
        jd = json.loads(request.body)
        # insert into administrador values (nombreadmin, appatadmin, apmatadmin, contraadmin, correoadmin)
        Administrador.objects.create(
            nombreadmin=jd['nombreadmin'],  # Se obtienen los valores del JSON
            appatadmin=jd['appatadmin'],  # Se obtienen los valores del JSON
            apmatadmin=jd['apmatadmin'],  # Se obtienen los valores del JSON
            contraadmin=jd['contraadmin'],  # Se obtienen los valores del JSON
            correoadmin=jd['correoadmin'],  # Se obtienen los valores del JSON
        )
        # Se envia un mensaje de exito
        datitos = {'message': "Operación exitosa"}
        # Se envia la respuesta al cliente en formato JSON
        return JsonResponse(datitos)

    def put(self, request, correo):
        """"Método PUT para modificar un registro en la tabla Administrador"""
        try:
            # Se obtiene el JSON enviado por el cliente
            jd = json.loads(request.body)
            # Se obtiene el registro a modificar
            administrador = Administrador.objects.get(
                correoadmin=correo)
            # Se asignan los nuevos valores
            administrador.nombreadmin = jd['nombreadmin']
            administrador.appatadmin = jd['appatadmin']
            administrador.apmatadmin = jd['apmatadmin']
            administrador.contraadmin = jd['contraadmin']
            administrador.correoadmin = jd['correoadmin']
            # Se guardan los cambios
            # update administrador set nombreadmin = nombreadmin, appatadmin = appatadmin, apmatadmin = apmatadmin, contraadmin = contraadmin, correoadmin = correoadmin where correoadmin = correo
            administrador.save()
            # Se envia un mensaje de exito
            datitos = {'message': "Operación exitosa"}
        # Excepción por si no existe el registro
        except ObjectDoesNotExist:
            datitos = {'message': "No existe el administrador o la administradora"}
        # Se envia la respuesta al cliente
        return JsonResponse(datitos)

    def delete(self, request, correo):
        """Método DELETE para eliminar un registro en la tabla Administrador"""
        try:
            # Se obtiene el registro a eliminar
            administrador = Administrador.objects.get(correoadmin=correo)
            # Se elimina el registro
            # delete from administrador where correoadmin = correo
            administrador.delete()
            # Se envia un mensaje de exito
            datitos = {'message': "Operación exitosa"}
        # Excepción por si no existe el registro
        except ObjectDoesNotExist:
            datitos = {'message': "No existe el administrador o la administradora"}
        # Se envia la respuesta al cliente
        return JsonResponse(datitos)


class CatalogozonasView(View):
    """Esta clase es una vista para el modelo o entidad Catalogozonas donde se establecen los métodos HTTP (GET, POST, PUT, DELETE)"""

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        # Se desactiva el CSRF para poder hacer peticiones desde el cliente
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        """Metodo GET para realizar consultas de la tabla Catalogozonas"""
        if id > 0:  # Si se envia un id, se obtiene un registro en especifico
            # select * from catalogozonas where idzona = id
            zonas = list(Catalogozonas.objects.filter(idzona=id).values())
            if len(zonas) > 0: # Si existe el registro
                zona = zonas[0]
                datitos = {'message': "Operacion exitosa", 'zona': zona}
            else: # Si no existe el registro
                datitos = {'message': "No existe la zona"}
        else:  # Si no se envia un id, se obtienen todos los registros
            # select * from catalogozonas
            zonas = list(Catalogozonas.objects.values())
            if len(zonas) > 0: # Si existe el registro
                datitos = {'message': "Operacion exitosa", 'zonas': zonas}
            else: # Si no existe el registro
                datitos = {'message': "No hay zonas"}
        # Se envia la respuesta al cliente en formato JSON
        return JsonResponse(datitos)

    def post(self, request):
        """Método POST para insertar un registro en la tabla Catalogozonas"""
        # Se obtiene el JSON enviado por el cliente
        jd = json.loads(request.body)
        # insert into catalogozonas values (colonia, codigopostal)
        Catalogozonas.objects.create(
            colonia=jd['colonia'], # Se obtienen los valores del JSON
            codigopostal=jd['codigopostal'], # Se obtienen los valores del JSON
        )
        # Se envia un mensaje de exito
        datitos = {'message': "Operación exitosa"}
        # Se envia la respuesta al cliente en formato JSON
        return JsonResponse(datitos)

    def put(self, request, id):
        """"Método PUT para modificar un registro en la tabla Catalogozonas"""
        try:
            # Se obtiene el JSON enviado por el cliente
            jd = json.loads(request.body)
            # Se obtiene el registro a modificar
            zona = Catalogozonas.objects.get(idzona=id)
            # Se asignan los nuevos valores
            zona.colonia = jd['colonia']
            zona.codigopostal = jd['codigopostal']
            # Se guardan los cambios
            # update catalogozonas set colonia = colonia, codigopostal = codigopostal where idzona = id
            zona.save()
            # Se envia un mensaje de exito
            datitos = {'message': "Operación exitosa"}
        # Excepción por si no existe el registro
        except ObjectDoesNotExist:
            datitos = {'message': "No existe la zona"}
        # Se envia la respuesta al cliente en formato JSON
        return JsonResponse(datitos)

    def delete(self, request, id):
        """Método DELETE para eliminar un registro en la tabla Catalogozonas"""
        try:
            # Se obtiene el registro a eliminar
            zona = Catalogozonas.objects.filter(idzona=id).values()
            # Se elimina el registro
            # delete from catalogozonas where idzona = id
            zona.delete()
            # Se envia un mensaje de exito
            datitos = {'message': "Operación exitosa"}
        # Excepción por si no existe el registro
        except ObjectDoesNotExist:
            datitos = {'message': "No existe la zona"}
        # Se envia la respuesta al cliente en formato JSON
        return JsonResponse(datitos)


class ClienteView(View):
    """Esta clase es una vista para el modelo o entidad Cliente donde se establecen los métodos HTTP (GET, POST, PUT, DELETE)"""

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        # Se desactiva el CSRF para poder hacer peticiones desde el cliente
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0, correo=""):
        """Metodo GET para realizar consultas de la tabla Cliente"""
        print('id: ' + str(id))
        print('correo: ' + correo)
        if id > 0:  # Si se envia un id, se obtiene un registro en especifico
            # select * from cliente where idcliente = id
            clientes = list(Cliente.objects.filter(idcliente=id).values())
            if len(clientes) > 0: # Si existe el registro
                cliente = clientes[0]
                datitos = {'message': "Operacion exitosa", 'cliente': cliente}
            else: # Si no existe el registro
                datitos = {'message': "No existe el cliente"}
        elif correo != "":  # Si se envia un correo, se obtiene un registro en especifico
            # select * from cliente where correocliente = correo
            clientes = list(Cliente.objects.filter(correocliente=correo).values())
            if len(clientes) > 0: # Si existe el registro
                cliente = clientes[0]
                datitos = {'message': "Operacion exitosa", 'cliente': cliente}
        else:  # Si no se envia un id ni un correo, se obtienen todos los registros
            clientes = list(Cliente.objects.values())
            if len(clientes) > 0: # Si existe el registro
                datitos = {'message': "Operacion exitosa",
                            'clientes': clientes}
            else: # Si no existe el registro
                datitos = {'message': "No hay clientes"}
        # Se envia la respuesta al cliente en formato JSON
        return JsonResponse(datitos)

    def post(self, request):
        """Método POST para insertar un registro en la tabla Cliente"""
        # Se obtiene el JSON enviado por el cliente
        jd = json.loads(request.body)
        # insert into cliente values (nombrecliente, appatcliente, apmatcliente, contracliente, correocliente, callecliente, colcliente, numextcliente, cpcliente)
        Cliente.objects.create(
            idcliente=jd['idcliente'],
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
        # Se envia un mensaje de exito
        datitos = {'message': "Operación exitosa"}
        # Se envia la respuesta al cliente en formato JSON
        return JsonResponse(datitos)

    def put(self, request, id):
        """"Método PUT para modificar un registro en la tabla Cliente"""
        try:
            # Se obtiene el JSON enviado por el cliente
            jd = json.loads(request.body)
            # Se obtiene el registro a modificar
            cliente = Cliente.objects.get(idcliente=id)
            # Se asignan los nuevos valores
            cliente.nombrecliente = jd['nombrecliente']
            cliente.appatcliente = jd['appatcliente']
            cliente.apmatcliente = jd['apmatcliente']
            cliente.contracliente = jd['contracliente']
            cliente.correocliente = jd['correocliente']
            cliente.callecliente = jd['callecliente']
            cliente.colcliente = jd['colcliente']
            cliente.numextcliente = jd['numextcliente']
            cliente.cpcliente = jd['cpcliente']
            # Se envia un mensaje de exito
            datitos = {'message': "Operación exitosa"}
        # Excepción por si no existe el registro
        except ObjectDoesNotExist:
            datitos = {'message': "No existe el o la cliente"}
        # Se envia la respuesta al cliente en formato JSON
        return JsonResponse(datitos)

    def delete(self, request, id):
        """Método DELETE para eliminar un registro en la tabla Cliente"""
        try:
            # Se obtiene el registro a eliminar
            cliente = Cliente.objects.filter(idcliente=id).values()
            # Se elimina el registro
            # delete from cliente where idcliente = id
            cliente.delete()
            # Se envia un mensaje de exito
            datitos = {'message': "Operación exitosa"}
        # Excepción por si no existe el registro
        except ObjectDoesNotExist:
            # Se envia un mensaje de error
            datitos = {'message': "No existe el o la cliente"}
        # Se envia la respuesta al cliente en formato JSON
        return JsonResponse(datitos)

class ReportefallasView(View):
    """Esta clase es una vista para el modelo o entidad Reportefallas donde se establecen los métodos HTTP (GET, POST, PUT, DELETE)"""

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        # Se desactiva el CSRF para poder hacer peticiones desde el cliente
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        """Metodo GET para realizar consultas de la tabla Reportefallas"""
        if id > 0:  # Si se envia un id, se obtiene un registro en especifico
            reportes = list(Reportefallas.objects.filter(
                idfalla=id).values())
            if len(reportes) > 0: # Si existe el registro
                reporte = reportes[0]
                datitos = {'message': "Operacion exitosa", 'reporte': reporte}
            else: # Si no existe el registro
                datitos = {'message': "No existe el reporte"}
        else:  # Si no se envia un id, se obtienen todos los registros
            reportes = list(Reportefallas.objects.values())
            if len(reportes) > 0: # Si existe el registro
                datitos = {'message': "Operacion exitosa",
                            'reportes': reportes}
            else: # Si no existe el registro
                datitos = {'message': "No hay reportes"}
        # Se envia la respuesta al cliente en formato JSON
        return JsonResponse(datitos)

    def post(self, request):
        """Método POST para insertar un registro en la tabla Reportefallas"""
        # Se obtiene el JSON enviado por el cliente
        jd = json.loads(request.body)
        # insert into reportefallas values (motivorep, fecharep, estatusrep, clavecliente)
        Reportefallas.objects.create(
            motivorep=jd['motivorep'],  # Se obtienen los valores del JSON
            fecharep=jd['fecharep'],  # Se obtienen los valores del JSON
            estatusrep=jd['estatusrep'],  # Se obtienen los valores del JSON
            clavecliente=jd['clavecliente']  # Se obtienen los valores del JSON
        )
        # Se envia un mensaje de exito
        datitos = {'message': "Operación exitosa"}
        # Se envia la respuesta al cliente en formato JSON
        return JsonResponse(datitos)

    def put(self, request, id):
        """"Método PUT para modificar un registro en la tabla Reportefallas"""
            # Se obtiene el JSON enviado por el cliente
        try:
            jd = json.loads(request.body)
            # Se obtiene el registro a modificar
            reporte = Reportefallas.objects.get(idfalla=id)
            # Se asignan los nuevos valores
            reporte.motivorep = jd['motivorep']
            reporte.fecharep = jd['fecharep']
            reporte.estatusrep = jd['estatusrep']
            reporte.clavecliente = jd['clavecliente']
            # Se envia un mensaje de exito
            datitos = {'message': "Operación exitosa"}
        # Excepción por si no existe el registro
        except ObjectDoesNotExist:
            datitos = {'message': "No existe el reporte"}
        # Se envia la respuesta al cliente en formato JSON
        return JsonResponse(datitos)

    def delete(self, request, id):
        """Método DELETE para eliminar un registro en la tabla Reportefallas"""
        try:
            # Se obtiene el registro a eliminar
            reporte = Reportefallas.objects.filter(idfalla=id).values()
            # Se elimina el registro
            # delete from reportefallas where idfalla = id
            reporte.delete()
            # Se envia un mensaje de exito
            datitos = {'message': "Operación exitosa"}
        # Excepción por si no existe el registro
        except ObjectDoesNotExist:
            datitos = {'message': "No existe el reporte"}
        # Se envia la respuesta al cliente en formato JSON
        return JsonResponse(datitos)
