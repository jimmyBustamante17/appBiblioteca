from django import forms
from appBiblioteca.models import *

class crearUsuario(forms.ModelForm):
    class Meta:
        model = Usuario

        fields = [
            'cedula',
            'nombre',
            'idRol'
        ]

        labels = {
            'cedula': 'Cedula',
            'nombre': 'Nombre',
            'idRol': 'Rol'
        }

        widgets = {
            'cedula': forms.TextInput(attrs={'class':'form-control w-25'}),
            'nombre': forms.TextInput(attrs={'class':'form-control w-25'}),
            'idRol': forms.Select(attrs={'class':'form-control w-25'}),
        }


class registrarMaterial(forms.ModelForm):
    class Meta:
        model = Material

        fields = [
            'identificador',
            'titulo',
            'cantidadRegistrada',
            'cantidadActual'
        ]

        labels = {
            'identificador':'Identificador',
            'titulo': 'Titulo',
            'cantidadRegistrada':'Cantidad',
            'cantidadActual':''
        }

        widgets = {
            'identificador': forms.TextInput(attrs={'class':'form-control w-25'}),
            'titulo': forms.TextInput(attrs={'class':'form-control w-25'}),
            'cantidadRegistrada': forms.NumberInput(attrs={'class':'form-control w-25','oninput':'actualizarCantidad()'}),
            'cantidadActual': forms.NumberInput(attrs={'class':'form-control w-25', 'style':'display:none'}),
            }