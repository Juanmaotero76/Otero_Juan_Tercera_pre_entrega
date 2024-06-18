from django.urls import path
from . import views


urlpatterns = [
    path('motores/', views.motores.as_view(), name='motores'),
    path('motores/crear/', views.crearmotores.as_view(), name='crear_motores'),
      
    


]