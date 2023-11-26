# from django.contrib.auth.backends import ModelBackend
# from api.models import *
# from django.core.exceptions import ObjectDoesNotExist

# class AdministradorBackend(ModelBackend):
#     def authenticate(self, request, correoadmin=None, contraadmin=None, **kwargs):
#         try:
#             if correoadmin is not None:
#                 user = Administrador.objects.get(correoadmin=correoadmin)
#             else:
#                 return None

#             if user.check_password(contraadmin):
#                 return user
            
#         except ObjectDoesNotExist:
#             return None
        
# class ClienteBackend(ModelBackend):
#     def authenticate(self, request, idcliente=None, correocliente=None, contracliente=None, **kwargs):
#         try:
#             if idcliente is not None:
#                 user = Cliente.objects.get(idcliente=idcliente)
#             elif correocliente is not None:
#                 user = Cliente.objects.get(correocliente=correocliente)
#             else:
#                 return None

#             if user.check_password(contracliente):
#                 return user
#         except ObjectDoesNotExist:
#             return None