from django import forms

class CrearUsuarioForm(forms.Form):
    nombre=forms.CharField(max_length=20)
    apellido=forms.CharField(max_length=20)
    email=forms.CharField(max_length=20)
    contrasenia=forms.CharField(max_length=20)

class BuscarUsuario(forms.Form):
    nombre=forms.CharField(max_length=20, required=False)