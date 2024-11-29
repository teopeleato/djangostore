from django.db import models
import datetime

class Evento(models.Model):
    codigo_i3a = models.IntegerField()
    titulo = models.CharField(max_length=100)
    titulo_largo = models.CharField(max_length=255)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='eventos/')
    fecha_inicio = models.DateField(default=datetime.date.today)  
    fecha_fin = models.DateField(default=datetime.date.today)
    descripcion = models.TextField(default='more info...')

    def __str__(self):
        return self.titulo

