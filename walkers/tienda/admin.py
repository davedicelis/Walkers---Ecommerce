from django.contrib import admin
from .models  import Cliente , Categoria , Producto ,Pedido
 #Subcategoria,
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Categoria)
# admin.site.register(Subcategoria)
admin.site.register(Producto)
admin.site.register(Pedido)
