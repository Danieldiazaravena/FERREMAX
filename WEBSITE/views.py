from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import *
from django.db.models import Q

def Base(request):

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

    return render(request,'base.html', context)

# VISTA LOGIN
def Login(request):

    return render(request,'login.html')


def Woi(request):

    return render(request, 'woi.html')


# VISTA LANDING
def Landing(request):

    return render(request, 'landing.html')

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

    if request.method == "POST":
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("landing")
    else:
        form = FormularioRegistro()

    return render(request, 'registration/register.html',{"form":form})
    
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

    productos = Producto.objects.all()
    marcas = Marca.objects.all()
    categorias = Categoria.objects.all()

    palabra_clave = request.GET.get('palabra_clave')
    tipo_producto = request.GET.get('tipo_producto')
    marca = request.GET.get('marca')
    precio = request.GET.get('precio')
    stock_disponible = request.GET.get('stock_disponible')

    if palabra_clave:
        productos = productos.filter(Q(nombre_producto__icontains=palabra_clave) | Q(descripcion__icontains=palabra_clave))
    if tipo_producto:
        productos = productos.filter(id_categoria=tipo_producto)
    if marca:
        productos = productos.filter(id_marca=marca)
    if precio==1:
        productos = productos.order_by('precio')
    elif precio==2:
        productos = productos.order_by('-precio')

    context = {     
        "productos": productos,
        "marcas": marcas,
        "categorias" : categorias
    }

    

    return render(request, 'catalogo.html', context)
