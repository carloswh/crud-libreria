from django.contrib import admin
from .models import Libro, Editor, Autor

# Register your models here.

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'email')

class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'editor', 'fecha_publicacion')
    list_filter = ('fecha_publicacion',)
    date_hierarchy = 'fecha_publicacion'
    ordering = ('-fecha_publicacion',)
    filter_horizontal = ('autores',)

admin.site.register(Editor)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Autor, AutorAdmin)