from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from .models import motores


class motores(ListView):
    model=motores
    template_name= 'motores/motores.html'  
    context_object_name = 'motores'  

class crearmotores(CreateView):
    model=motores
    template_name= 'motores/crear_motores.html'  
    success_url=reverse_lazy(motores)
    fields=[ 'combustible', 'cilindrada','marca','fecha']  
    
    
class editarmotores(UpdateView):
    ...