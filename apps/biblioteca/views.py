from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Autor, Editor, Libro
from .forms import AutorForm, EditorForm, LibroForm

# Create your views here.

class AutorListView(ListView):
    model = Autor
    template_name = "autor/autores.html"
    context_object_name = 'autores'

class AutorCreateView(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = "autor/new.html"
    success_url = reverse_lazy('biblioteca:autor_list')

class AutorUpdateView(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = "autor/new.html"
    success_url = reverse_lazy('biblioteca:autor_list')

def AutorDelete(request, id):
    autor = Autor.objects.get(id = id)

    if autor:
        autor.delete()
    return HttpResponseRedirect(reverse_lazy('biblioteca:editor_list'))



class EditorListView(ListView):
    model = Editor
    template_name = "editor/editores.html"
    context_object_name = 'editores'

class EditorCreateView(CreateView):
    model = Editor
    form_class = EditorForm
    template_name = "editor/new.html"
    success_url = reverse_lazy('biblioteca:editor_list')

class EditorUpdateView(UpdateView):
    model = Editor
    form_class = EditorForm
    template_name = "editor/new.html"
    success_url = reverse_lazy('biblioteca:editor_list')

def EditorDelete(request, id):
    editor = Editor.objects.get(id = id)

    if editor:
        editor.delete()
    return HttpResponseRedirect(reverse_lazy('biblioteca:editor_list'))



class LibroListView(ListView):
    model = Libro
    template_name = "libro/libros.html"
    context_object_name = 'libros'

class LibroCreateView(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = "libro/new.html"
    success_url = reverse_lazy('biblioteca:libro_list')

class LibroUpdateView(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = "libro/new.html"
    success_url = reverse_lazy('biblioteca:libro_list')

def LibroCreate(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)

        if form.is_valid():
            form.save()
            #return HttpResponseRedirect('biblioteca/libros')
            return HttpResponseRedirect(reverse_lazy('biblioteca:libro_list'))
        else:
            print (form.errors)
    else:
        form = LibroForm()
    
    return render(request, 'libro/new.html', { 'form': form })

def LibroDelete(request, id):
    libro = Libro.objects.get(id = id)

    if libro:
        libro.delete()
    return HttpResponseRedirect(reverse_lazy('biblioteca:libro_list'))

