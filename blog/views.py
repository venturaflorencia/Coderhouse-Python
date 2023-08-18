from django.shortcuts import render, redirect
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from blog.models import Posteo

# Create your views here.

class PosteoListView(ListView):
   model = Posteo
   template_name = 'blog/lista_posteos.html' 


class PosteoCreateView(LoginRequiredMixin,CreateView):
   model = Posteo
   fields = ('titulo', 'bajada', 'creador', 'imagen', 'texto','fecha_publicacion' )
   success_url = reverse_lazy('lista_posteos')

class PosteoDetailView(DetailView):
   model = Posteo
   success_url = reverse_lazy('lista_posteos')

class PosteoUpdateView(LoginRequiredMixin,UpdateView):
   model = Posteo
   fields = ('titulo', 'bajada', 'creador', 'imagen', 'texto', 'fecha_publicacion' )
   success_url = reverse_lazy('lista_posteos')

class PosteoDeleteView(LoginRequiredMixin,DeleteView):
   model = Posteo
   success_url = reverse_lazy('lista_posteos')


def buscar_posteo(request):
   if request.method == "POST":
       data = request.POST
       busqueda = data["busqueda"]
       posteos = Posteo.objects.filter(titulo__contains=busqueda)
       
       if busqueda == "":
          posteos = Posteo.objects.all().order_by('-fecha_publicacion')
          contexto = {
           "posteos": posteos,
            }
       
       
       else:
         contexto = {
            "posteos": posteos,
         }
       http_response = render(
           request=request,
           template_name='inicio.html',
           context=contexto,
       )
       return http_response
   
