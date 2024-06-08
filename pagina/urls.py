from django.urls import path
from pagina import views


urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('loguin/', views.loguin, name='loguin'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('ver_usuarios/', views.ver_usuarios, name='ver_usuarios'),
    path('busqueda_cliente/', views.busqueda_cliente, name='busqueda_cliente'),
    path('buscar/', views.buscar, name='buscar'),


]