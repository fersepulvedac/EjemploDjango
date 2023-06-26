from rest_framework import serializers
from core.models import Producto
from .models import Suscripcion

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        exclude = ['codigo', 'detalle', 'precio', 'imagen', 'stock']

class SuscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suscripcion
        fields = ['user', 'suscrito']