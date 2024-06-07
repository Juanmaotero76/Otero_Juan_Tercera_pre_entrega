from django.db import models

#Create your models here.
class cliente(models.Model):
    nombre  = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    contrasenia = models.CharField(max_length=20, default='123456')
    def __str__(self):
        return f'cliente {self.nombre} {self.apellido}'
