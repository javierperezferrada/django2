from django.db import models

class Imagen(models.Model):
	imagen = models.ImageField(upload_to='galeria')
	nombre = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=150)
	tags = models.CharField(max_length=150)
	