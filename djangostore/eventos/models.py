from django.db import models
import datetime

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    titulo_largo = models.CharField(max_length=255)
    precio_base = models.IntegerField()
    imagen = models.ImageField(upload_to='eventos/')
    fecha_inicio = models.DateField(default=datetime.date.today)  
    fecha_fin = models.DateField(default=datetime.date.today)
    descripcion = models.TextField(default='more info...')

    def __str__(self):
        return self.titulo

