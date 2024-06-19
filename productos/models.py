from django.db import models

# Create your models here.
class Motores(models.Model):
    combustible = models.CharField(max_length=20)
    cilindrada = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    fecha = models.DateField()
    
    # class Meta:
    #     model= models
    #     fields=[ 'combustible', 'cilindrada','marca','fecha']  
    # #      # Optional model configuration (e.g., app_label, etc.)
    #     help_texts = {key: '' for key in fields}
        
    def __str__(self):
        return f'{self.combustible} {self.cilindrada} {self.marca} {self.fecha}'