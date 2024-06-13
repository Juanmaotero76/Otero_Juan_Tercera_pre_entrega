from django.urls import path
from pagina import views


urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('loguin/', views.loguin, name='loguin'), # para el futuro
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('ver_usuarios/', views.ver_usuarios, name='ver_usuarios'),
    path('busqueda_cliente/', views.busqueda_cliente, name='busqueda_cliente'),
    path('contacto/', views.contacto, name='contacto'),
    path('about/', views.about, name='about'),
    path('eliminar_usuario/<int:id>', views.eliminar_usuario, name='eliminar_usuario')
    


]