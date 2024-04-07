from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import *

def Base(request):

   return render(request,'base.html')

# VISTA LOGIN
def Login(request):
    if request.user.groups.filter(name="vendedor").exists():
        grupo = "vendedor"
    elif request.user.groups.filter(name="bodeguero").exists():
        grupo = "bodeguero"
    elif request.user.groups.filter(name="contador").exists():
        grupo = "contador"
    else:
        grupo = "cliente"

    context = {
        "grupo": grupo,
    }

    return render(request,'login.html', context)


# VISTA LANDING
def Landing(request):
    if request.user.groups.filter(name="vendedor").exists():
        grupo = "vendedor"
    elif request.user.groups.filter(name="bodeguero").exists():
        grupo = "bodeguero"
    elif request.user.groups.filter(name="contador").exists():
        grupo = "contador"
    else:
        grupo = "cliente"

<<<<<<< HEAD
    return render(request, 'landing.html')

def Woi(request):

    return render(request, 'woi.html')
=======
    context = {
        "grupo": grupo,
    }

    return render(request, 'landing.html', context)

# formulario para registrarse
class FormularioRegistro(UserCreationForm):
    email = forms.EmailField(
        max_length=254, help_text="Required. Enter a valid email address."
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        
# VISTA REGISTRO
def Register(request):
    if request.user.groups.filter(name="vendedor").exists():
        grupo = "vendedor"
    elif request.user.groups.filter(name="bodeguero").exists():
        grupo = "bodeguero"
    elif request.user.groups.filter(name="contador").exists():
        grupo = "contador"
    else:
        grupo = "cliente"

    context = {
        "grupo": grupo,
    }

    if request.method == "POST":
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("landing")
    else:
        form = FormularioRegistro()
    return render(request,'registration/register.html', {"form": form}, context)
    
#VISTA PARA AGREGAR NUEVOS PRODUCTOS
@login_required
def Agregar(request):
    if request.user.groups.filter(name="vendedor").exists():
        grupo = "vendedor"
    elif request.user.groups.filter(name="bodeguero").exists():
        grupo = "bodeguero"
    elif request.user.groups.filter(name="contador").exists():
        grupo = "contador"
    else:
        grupo = "cliente"


    cat = Categoria.objects.raw("select * from website_categoria")

    if request.method == "POST":
        nombre_producto = request.POST["nombre"]
        precio = request.POST["precio"]
        descripcion = request.POST["descripción"]
        categoria = request.POST["categoria"]
        objCategoria = Categoria.objects.get(id_categoria=categoria)
        objProducto = Producto.objects.create(
            nombre_producto=nombre_producto,
            precio=precio,
            descripcion=descripcion,
            id_categoria=objCategoria,
        )

        imagen = request.FILES.get("imagen")
        Imagen_producto.objects.create(
            imagen_producto=imagen,
            id_producto=objProducto
        )
        context = {
            "mensaje": "Oferta publicada exitosamente",
            "grupo": grupo,
            "cat": cat,
            }
        return render(request, "agregar.html", context)
    else:
        context = {
            "grupo": grupo,
            "cat": cat,
            }
        return render(request, "agregar.html", context)
    
def Catalogo(request):
    if request.user.groups.filter(name="vendedor").exists():
        grupo = "vendedor"
    elif request.user.groups.filter(name="bodeguero").exists():
        grupo = "bodeguero"
    elif request.user.groups.filter(name="contador").exists():
        grupo = "contador"
    else:
        grupo = "cliente"

    productos = Producto.objects.select_related(
                "id_categoria"
                )

    context = {
        "grupo": grupo,
        "productos": productos,
    }

    return render(request, 'catalogo.html', context)
>>>>>>> 756924f3d7b5b9b839217d0aa57fcf5fad41e17f
