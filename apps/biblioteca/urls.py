from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^autores/$', views.AutorListView.as_view(), name='autor_list'),
    url(r'^autores/new/$', views.AutorCreateView.as_view(), name='autor_create'),
    url(r'^autores/edit/(?P<pk>\d+)/$', views.AutorUpdateView.as_view(), name='autor_edit'),
    url(r'^autores/delete/(?P<id>\d+)/$', views.AutorDelete, name='autor_delete'),

    url(r'^editores/$', views.EditorListView.as_view(), name='editor_list'),
    url(r'^editores/new/$', views.EditorCreateView.as_view(), name='editor_create'),
    url(r'^editores/edit/(?P<pk>\d+)/$', views.EditorUpdateView.as_view(), name='editor_edit'),
    url(r'^editores/delete/(?P<id>\d+)/$', views.EditorDelete, name='editor_delete'),

    url(r'^libros/$', views.LibroListView.as_view(), name='libro_list'),
    url(r'^libros/new/$', views.LibroCreate, name='libro_create'),
    url(r'^libros/edit/(?P<pk>\d+)/$', views.LibroUpdateView.as_view(), name='libro_edit'),
    url(r'^libros/delete/(?P<id>\d+)/$', views.LibroDelete, name='libro_delete'),
]

