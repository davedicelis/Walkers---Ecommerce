from django.urls import re_path
from .views import ProductoListApi , CategoriaListApi , ClienteListApi  ,PedidoCreateApi, ProductoCreateApi ,CategoriaCreateApi

app_name = 'tienda'

urlpatterns = [
 re_path("productos", ProductoListApi.as_view(), name="productos"),
 re_path("categoria", CategoriaListApi.as_view(), name="categoria"),
 re_path("cliente", ClienteListApi.as_view(), name="cliente"),
 re_path("crearpedido", PedidoCreateApi.as_view(), name="crearpedido"),
 re_path("crearproducto", ProductoCreateApi.as_view(), name="crearproducto"),
 re_path("crearcategoria", CategoriaCreateApi.as_view(), name="crearcategorias"),
]
