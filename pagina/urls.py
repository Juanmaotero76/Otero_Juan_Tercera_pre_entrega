from django.urls import path
from pagina import views


urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('loguin/', views.loguin, name='loguin'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    # path('template1/<str:nombre>/<str:apellido>/<int:edad>', views.template1),
    # path('template2/<str:nombre>/<str:apellido>/<int:edad>', views.template2),
    # path('template3/<str:nombre>/<str:apellido>/<int:edad>', views.template3),
    # path('template4/<str:nombre>/<str:apellido>/<int:edad>', views.template4),
    # path('prueba/', views.probando, name="probando"),
    # path('autos/crear/<str:marca>/<str:modelo>/', views.crear_auto, name='crear_auto')
]