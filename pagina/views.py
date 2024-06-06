from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader

def inicio (request):
    #return HttpResponse('Inicio capo total')
    return render(request, 'inicio/index.html')

# Create your views here.
def loguin (request):
    return render (request, 'loguin.html' )

def crear_usuario (request):
    
    return render (request, 'nuevo_usuario.html')