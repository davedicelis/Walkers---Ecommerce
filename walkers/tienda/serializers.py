from .models import Cliente , Categoria ,Producto ,Pedido
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import (SerializerMethodField)
from rest_framework import serializers

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializer(ModelSerializer):
    categoria = CategoriaSerializer(many=True)
    class Meta:
        model = Producto
        fields = '__all__'
      
       
class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class PedidoSerializer(ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'