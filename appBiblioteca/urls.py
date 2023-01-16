from django.contrib import admin
from django.urls import path
from appBiblioteca.views import *

urlpatterns = [
    path('base/',base),
    path('registro/',registro, name="Registro"),
    path('materiales/',Materiales, name="Materiales"),
    path('usuarios/',Usuarios, name="Usuarios"),
    path('eliminarUsuario/<str:cedulaUser>',elimianrUsuario, name="eliminarUsuarios"),
    path('incrementarMaterial/<int:identificador>',incrementarMaterial, name="incrementarMaterial"),
    path('prestarMaterial/<int:cedula>',prestarMaterial, name="prestarMaterial"),
    path('prestar/<int:cedula>/<int:identificador>',prestar, name="prestar"),
    path('devolucion/<int:cedula>/<int:identificador>',devolucion, name="devolucion"),
    path('materialesPrestados/<int:cedula>',materialesPrestados, name="materialesPrestados"),
]