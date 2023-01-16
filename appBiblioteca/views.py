from django.shortcuts import render, redirect
from django.template import Template, Context
from django.http import HttpResponse
from appBiblioteca.models import *
from appBiblioteca.forms import *

# Create your views here.
def Usuarios(request):
    usuarios = Usuario.objects.all()
    if request.method == 'POST':
        form = crearUsuario(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Usuarios")
        else:
            return render(request, 'usuarios.html', {'usuarios': usuarios, 'form': form})
    else:
        form = crearUsuario()
        return render(request, 'usuarios.html',{'form':form, 'usuarios': usuarios}, )


# MATERIALES
def Materiales(request):
    materiales = Material.objects.all()
    if request.method == 'POST':
        form = registrarMaterial(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Materiales")
        else:
            return render(request, 'materiales.html', {'materiales': materiales, 'form': form})
    else:
        form = registrarMaterial()
        return render(request, 'materiales.html', {'materiales': materiales, 'form': form})


def elimianrUsuario(request, cedulaUser):
    eliminar = Usuario.objects.get(cedula=cedulaUser)
    materialesPrestados = MaterialPrestado.objects.filter(cedula = cedulaUser)
    if len(materialesPrestados) == 0:
        eliminar.delete()
        return redirect("Usuarios")
    else:
        return redirect("Usuarios")

def incrementarMaterial(request, identificador):
    material = Material.objects.get(identificador = identificador)
    if request.method == 'POST':
        cantidad = int(request.POST.get("cantidad"))
        material.cantidadRegistrada += cantidad
        material.cantidadActual += cantidad 
        material.save()
        return redirect('Materiales')
    else:
        return render(request, 'incrementarMaterial.html')

def prestarMaterial(request, cedula):
    materiales = Material.objects.all()
    return render(request, 'prestarMaterial.html', {'materiales':materiales, 'cedula':cedula})

def prestar(request, cedula, identificador):
    material = Material.objects.get(identificador = identificador)
    usuario  = Usuario.objects.get(cedula = cedula)
    material.cantidadActual -= 1
    material.save()
    generarRegistro(usuario,material,"Prestamo")
    MaterialPrestado.objects.create(cedula = usuario, idMaterial = material, cantidad=1)
    return redirect("prestarMaterial",cedula)

def devolucion(request, cedula, identificador):
    material = Material.objects.get(identificador = identificador)
    usuario  = Usuario.objects.get(cedula = cedula)
    material.cantidadActual += 1
    material.save()
    eliminar = MaterialPrestado.objects.filter(cedula = cedula).first()
    eliminar.delete()
    generarRegistro(usuario,material,"Devolución")
    return redirect("materialesPrestados",cedula)

def materialesPrestados(request, cedula):
    materialPrestado = MaterialPrestado.objects.filter(cedula = cedula)
    return render(request, 'materialesPrestados.html', {'materialPrestado':materialPrestado, 'cedula':cedula})


def generarRegistro(cedula,idMaterial,estado):
    Historial.objects.create(cedula = cedula, idMaterial  =idMaterial, estado = estado)

def base(request):
    return render(request, 'base.html')

def registro(request):
    historiales = Historial.objects.all()
    return render(request, 'historial.html', {'historiales': historiales})