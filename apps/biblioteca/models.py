from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Editor(models.Model):
    nombre      = models.CharField(max_length = 30)
    domicilio   = models.CharField(max_length = 50)
    ciudad      = models.CharField(max_length = 60)
    estado      = models.CharField(max_length = 30)
    pais        = models.CharField(max_length = 50)
    website     = models.URLField()
    created_at  = models.DateTimeField(auto_now_add = True)
    updated_at  = models.DateTimeField(auto_now = True)

    """ Se utiliza para definir un ordenamiento (opciones especificas) por default al obtener la coleccion """
    class Meta:
        ordering = ['nombre']
        verbose_name_plural = 'Autores'
    
    def __unicode__(self):
        return self.nombre 

class Autor(models.Model):
    nombre      = models.CharField(max_length = 30)
    apellidos   = models.CharField(max_length = 40)
    email       = models.EmailField(blank = True, verbose_name = 'e-mail')
    created_at  = models.DateTimeField(auto_now_add = True)
    updated_at  = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return "{} {}".format(self.nombre, self.apellidos)

class Libro(models.Model):
    titulo              = models.CharField(max_length = 100)
    autores             = models.ManyToManyField(Autor)
    editor              = models.ForeignKey(Editor, null = True, blank = True)
    fecha_publicacion   = models.DateField(blank = True, null = True)
    portada             = models.ImageField(blank = True, null = True, upload_to = 'portadas')
    created_at          = models.DateTimeField(auto_now_add = True)
    updated_at          = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return self.titulo
