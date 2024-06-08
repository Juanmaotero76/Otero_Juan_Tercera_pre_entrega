from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context, loader
from pagina.models import cliente
from pagina.forms import CrearUsuarioForm
def inicio (request):
    #return HttpResponse('Inicio capo total')
    return render(request, 'inicio/index.html')

# Create your views here.
def loguin (request):
    return render (request, 'loguin.html' )

# def crear_usuario (request, nombre, apellido, email, contrasenia):
#     Cliente=cliente(nombre=nombre, apellido=apellido, email=email, contrasenia=contrasenia)
#     Cliente.save()
#     return render (request, 'crear_usuario.html',  )

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

    print('Valor de la request: ', request)
    print('Valor de get: ' , request.GET)
    print('Valor de post: ' , request.POST)
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
    return render(request, 'ver_usuarios.html', {'clientes':clientes})

def busqueda_cliente(request):
    
    return render(request, 'busqueda_cliente.html')

def buscar(request):
    if request.POST['nombre']:
        user=request.POST['nombre']
        clientes=cliente.objects.filter(nombre=user)  
        return render(request, 'respuesta.html', {'clientes':clientes})
    else:
    
        respuesta= "No hay datos"
    #respuesta=f'Buscando el cliente {request.GET['nombre']}'
    return HttpResponse(respuesta)