from django.shortcuts import render
from rest_framework.generics import CreateAPIView,RetrieveUpdateAPIView,UpdateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView,DestroyAPIView
from .serializers import ProductoSerializer ,CategoriaSerializer , ClienteSerializer ,PedidoSerializer
from .models import Producto , Categoria , Cliente , Pedido

# Create your views here.
#@permission_classes((AllowAny, ))
class ProductoListApi(ListAPIView):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all().order_by('id')
    #queryset = Producto.objects.filter(precio__lte=350000)
    

class CategoriaListApi(ListAPIView):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all().order_by('id')


class ClienteListApi(ListAPIView):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all().order_by('id')

#CREATE
class PedidoCreateApi(CreateAPIView):
    serializer_class = PedidoSerializer
    queryset = Pedido.objects.all().order_by('id')

class ProductoCreateApi(CreateAPIView):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all().order_by('id')

class CategoriaCreateApi(CreateAPIView):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all().order_by('id')