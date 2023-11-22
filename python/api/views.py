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

    def get(self, request):
        administradores = list(Administrador.objects.values())
        if len(administradores) > 0:
            datitos = {'message': "Operacion exitosa", 'administradores': administradores}
        else:
            datitos = {'message': "No hay administradores"}
        return JsonResponse(datitos)

    def post(self, request):
        jd = json.loads(request.body)
        Administrador.objects.create(
            nombreadmin = jd['nombreadmin'],
            appatadmin = jd['appatadmin'],
            apmatadmin = jd['apmatadmin'],
            contraadmin = jd['contraadmin'],
            correoadmin = jd['correoadmin'],
        )
        datitos = {'message': "Operación exitosa"}
        return JsonResponse(datitos)
    
    def put(self, request):
        pass
    
    def delete(self, request):
        pass

class CatalogozonasView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request):
        zonas = list(Catalogozonas.objects.values())
        if len(zonas) > 0:
            datitos = {'message': "Operacion exitosa", 'administradores': zonas}
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
    
    def put(self, request):
        pass
    
    def delete(self, request):
        pass

class ClienteView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request):
        clientes = list(Cliente.objects.values())
        if len(clientes) > 0:
            datitos = {'message': "Operacion exitosa", 'administradores': clientes}
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
    
    def put(self, request):
        pass
    
    def delete(self, request):
        pass

class ReportefallasView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request):
        fallas = list(Reportefallas.objects.values())
        if len(fallas) > 0:
            datitos = {'message': "Operacion exitosa", 'administradores': fallas}
        else:
            datitos = {'message': "No hay fallas"}
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
    
    def put(self, request):
        pass
    
    def delete(self, request):
        pass