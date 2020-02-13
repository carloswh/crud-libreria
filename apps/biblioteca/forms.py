# -*- coding: utf-8 -*-

from django import forms
from .models import Autor, Editor, Libro

class AutorForm(forms.ModelForm):
    
    class Meta:
        model = Autor

        fields = [
            'nombre',
            'apellidos',
            'email',
        ]

        labels = {
            'nombre'    : 'Nombres',
            'apellidos' : 'Apellidos',
            'email'     : 'Correo electronico',
        }

        widgets = {
            'nombre'    : forms.TextInput(attrs = {'class' : 'form-control'}),
            'apellidos' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'email'     : forms.TextInput(attrs = {'class' : 'form-control'}),
        }

class EditorForm(forms.ModelForm):
    
    class Meta:
        model = Editor

        fields = [
            'nombre',
            'domicilio',
            'ciudad',
            'estado',
            'pais',
            'website',
        ]

        labels = {
            'nombre'    : 'Nombre completo',
            'domicilio' : 'Domicilio',
            'ciudad'    : 'Ciudad',
            'estado'    : 'Estado',
            'pais'      : 'Pais',
            'website'   : 'Página web',
        } 

        widgets = {
            'nombre'    : forms.TextInput(attrs = { 'class' : 'form-control' }),
            'domicilio' : forms.TextInput(attrs = { 'class' : 'form-control' }),
            'ciudad'    : forms.TextInput(attrs = { 'class' : 'form-control' }),
            'estado'    : forms.TextInput(attrs = { 'class' : 'form-control' }),
            'pais'      : forms.TextInput(attrs = { 'class' : 'form-control' }),
            'website'   : forms.TextInput(attrs = { 'class' : 'form-control' }),
        }

class LibroForm(forms.ModelForm):
    
    class Meta:
        model = Libro

        fields = [
            'titulo',
            'autores',
            'editor',
            'fecha_publicacion',
            'portada',
        ]

        labels = {
            'titulo'            : 'Titulo',
            'autores'           : 'Autores',
            'editor'            : 'Editor',
            'fecha_publicacion' : 'Fecha publicación',
            'portada'           : 'Portada',
        }

        widgets = {
            'titulo'            : forms.TextInput(attrs = { 'class' : 'form-control' }),
            'autores'           : forms.SelectMultiple(attrs = { 'class' : 'form-control' }),
            'editor'            : forms.Select(attrs = { 'class' : 'form-control' }),
            'fecha_publicacion' : forms.TextInput(attrs = { 'class' : 'form-control' }),
            'portada'           : forms.FileInput(attrs = { 'class' : 'form-control-file' })
        }