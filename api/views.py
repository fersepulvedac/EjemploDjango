from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework import status
from core.models import Producto, User

@api_view(['GET'])
def enOferta(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    data = ProductoSerializer(producto)
    return Response(data.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def suscrito(request, email):
    if request.method == 'GET':
        try:
            user = Suscripcion.objects.get(user=email)
            data = SuscripcionSerializer(user)
            return Response(data.data, status=status.HTTP_200_OK)
        except Suscripcion.DoesNotExist:
            return Response(data={"message":"Usuario no existe"}, status=status.HTTP_404_NOT_FOUND)
        
@api_view(['GET'])
def suscribir(request, email):
    if request.method == 'GET':
        try:
            user = Suscripcion.objects.get(user=email)
            serializer = SuscripcionSerializer(data=user)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Suscripcion.DoesNotExist:
            return Response(data={"message":"Usuario no existe"}, status=status.HTTP_404_NOT_FOUND)