from django.db import models

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    titulo_largo = models.CharField(max_length=255)
    precio_base = models.IntegerField()
    imagen = models.ImageField(upload_to='eventos/')

    def __str__(self):
        return self.titulo

