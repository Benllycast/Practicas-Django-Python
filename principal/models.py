#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Receta(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    ingredientes = models.TextField(help_text='redacta los ingredientes')
    preparacion = models.TextField(verbose_name='Preparacion')
    imagen = models.ImageField(upload_to='recetas', verbose_name = 'Imagen', null=True, blank=True)
    tiempo_registro = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.titulo
    
class Comentario(models.Model):
    receta = models.ForeignKey(Receta)
    texto = models.TextField(help_text='Tu comentario', verbose_name='Comentario')
    
    def __unicode__(self):
        return self.texto