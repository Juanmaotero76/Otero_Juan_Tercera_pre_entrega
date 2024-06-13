from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context, loader
from pagina.models import cliente
from pagina.forms import CrearUsuarioForm, BuscarUsuario, EditarUsuarioForm
def inicio (request):
    #return HttpResponse('Inicio capo total')
    return render(request, 'inicio/index.html')

# Create your views here.
def loguin (request):
    return render (request, 'loguin.html' )


def crear_usuario (request):
    # #V1
    # print('Valor de la request: ', request)
    # print('Valor de get: ' , request.GET)
    # print('Valor de post: ' , request.POST)
    # request.POST
    # if request.method == 'POST':
    #     Cliente=cliente(nombre=request.POST['nombre'], apellido=request.POST['apellido'], email=request.POST['email'], contrasenia=request.POST['contrasenia'])
    #     Cliente.save()
    # return render (request, 'crear_usuario.html' )

   
    request.POST
    formulario=CrearUsuarioForm()
    if request.method == 'POST':
        formulario=CrearUsuarioForm(request.POST)
        if formulario.is_valid():
            datos=formulario.cleaned_data
            Cliente=cliente(nombre=datos.get('nombre'), apellido=datos.get('apellido'), email=datos.get('email'), contrasenia=datos.get('contrasenia'))
            Cliente.save()
            return redirect('inicio')
        
    
   
    return render (request, 'crear_usuario.html',  {'formulario': formulario})

def ver_usuarios(request): 
    clientes=cliente.objects.all()
    formulario=BuscarUsuario(request.GET)
   
    return render(request, 'ver_usuarios.html', {'clientes':clientes})

def busqueda_cliente(request):
    formulario=BuscarUsuario(request.GET)
    if formulario.is_valid():
        nombre=formulario.cleaned_data['nombre']
        Cliente=cliente.objects.filter(nombre__icontains=nombre)  
         
    return render(request, 'busqueda_cliente.html',{'cliente':Cliente, 'formulario':formulario})

def eliminar_usuario(request, id):
    Cliente=cliente.objects.get(id=id)
    Cliente.delete()    
    return redirect('ver_usuarios')

def editar_usuario(request, id):
    Cliente=cliente.objects.get(id=id)
    formulario=EditarUsuarioForm(initial={'nombre': Cliente.nombre,'apellido': Cliente.apellido , 'email':Cliente.email, 'contrasenia':Cliente.contrasenia})
    if request.method == 'POST':  
        formulario=EditarUsuarioForm(request.POST)
        if formulario.is_valid():
            datos=formulario.cleaned_data
            Cliente.nombre=datos['nombre']
            Cliente.apellido=datos['apellido']
            Cliente.email=datos['email']
            Cliente.contrasenia=datos['contrasenia']
            Cliente.save()
            return redirect('inicio')
    
    
    
    return render(request, 'editar_usuario.html', {'formulario':formulario, 'cliente':Cliente})

     
 
    

def contacto (request):
    return render (request, 'contacto.html' )

def about (request):
    return render (request, 'about.html' )