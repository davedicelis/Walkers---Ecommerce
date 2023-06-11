from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Cliente(models.Model):
	nombre = models.CharField(max_length=200, null=True)
	telefono = models.CharField(max_length=10)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.nombre
	

class Categoria(models.Model):
	nombre=models.CharField(max_length=250)
	activo= models.BooleanField(default=True)
	imagen = models.ImageField(upload_to='images/', null=True)
	imagen2 = models.ImageField(upload_to='images/', null=True)
	
	def __str__(self):
		    return self.nombre	

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.IntegerField(null=True)
    categoria = models.ManyToManyField(Categoria)
    descripcion = models.CharField(max_length=200, default='')
    estado = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='images/', null=True)
    imagen2 = models.ImageField(upload_to='images/', null=True)


    def __str__(self):
        return self.nombre


	
class Pedido(models.Model):
	producto = models.ManyToManyField(Producto)
	cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
	cantidad = models.IntegerField(default=1)
	direccion = models.CharField(max_length=50, default='', blank=True)
	telefono = models.CharField(max_length=50, default='', blank=True)
	fecha = models.DateTimeField(null=True)

	def __str__(self):
		 return f'{self.id}'