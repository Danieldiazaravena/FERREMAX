from django.shortcuts import render, redirect
import django_filters 
import matplotlib.pyplot as plt
import io
import urllib, base64
from django.shortcuts import render, get_object_or_404, redirect
from django_filters import DateFilter
from django.shortcuts import get_object_or_404 
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
import requests
from .models import *
from django.db.models import Q
from .utils import get_dollar_value

# SDK de Mercado Pago (si da problemas, instalar con: pip install mercadopago)
import mercadopago
# Agrega credenciales
sdk = mercadopago.SDK("TEST-937485966507246-051120-5327fec403daba4a078a7d4a79547a6a-1774376550")
# Nombre de usuario comprador de prueba: TESTUSER518394180
# Contraseña: cCnwPtzVxv

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

def Woi(request):
    if request.user.groups.filter(name="vendedor").exists():
        grupo = "vendedor"
    elif request.user.groups.filter(name="bodeguero").exists():
        grupo = "bodeguero"
    elif request.user.groups.filter(name="contador").exists():
        grupo = "contador"
    else:
        grupo = "cliente"

    context = {
        "grupo":grupo
    }
    return render(request, 'woi.html',context)

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

    if request.user.is_authenticated:
        user_id = request.user.id
    else:
        # Manejar el caso del usuario no autenticado
        return redirect('login')  # Redirige al usuario a la página de inicio de sesión
    usuario = request.user
    carrito = Carrito.objects.filter(estado=0,usuario=usuario).first()
    contador=Carrito_item.objects.filter(id_carrito=carrito).count()

    context = {
        "contador" : contador,
        "grupo":grupo
    }
    return render(request, 'landing.html',context)

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
            Carrito.objects.create(usuario=user,estado=0)
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
    marcas = Marca.objects.raw("select * from website_marca")

    if request.method == "POST":
        nombre_producto = request.POST["nombre"]
        precio = request.POST["precio"]
        descripcion = request.POST["descripción"]
        categoria = request.POST["categoria"]
        marcaProd = request.POST["marca"]
        objCategoria = Categoria.objects.get(id_categoria=categoria)
        objMarca = Marca.objects.get(id_marca=marcaProd)
        objProducto = Producto.objects.create(
            nombre_producto=nombre_producto,
            precio=precio,
            descripcion=descripcion,
            id_categoria=objCategoria,
            id_marca=objMarca
        )

        imagen = request.FILES.get("imagen")
        Imagen_producto.objects.create(
            imagen_producto=imagen,
            id_producto=objProducto
        )

        #Creación del diccionario para enviar los datos a la API
        datos_api = {
                "id_producto": None,
                "nombre_producto": nombre_producto,
                "precio": precio,
                "descripcion": descripcion,
                "stock_bodega": 50,  # Inicialmente todo producto nuevo creado comienza con 50 stock en bodega
                "id_marca": marcaProd,
                "id_categoria": categoria,
                "grupo":grupo
            }

        #Envío de los datos a la API
        requests.post('http://localhost/api/api/post.php?', json=datos_api)



        context = {
            "mensaje": "Oferta publicada exitosamente",
            "grupo": grupo,
            "cat": cat,
            "marca": marcas
            }
        return render(request, "agregar.html", context)
    else:
        context = {
            "grupo": grupo,
            "cat": cat,
            "marca": marcas
            }
        return render(request, "agregar.html", context)
    
from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Categoria, Imagen_producto
from django.http import HttpResponseBadRequest

def Editar(request, pk):
    grupo = "cliente"
    if request.user.groups.filter(name="vendedor").exists():
        grupo = "vendedor"
    elif request.user.groups.filter(name="bodeguero").exists():
        grupo = "bodeguero"
    elif request.user.groups.filter(name="contador").exists():
        grupo = "contador"


    cat = Categoria.objects.all()

    cat = Categoria.objects.raw("select * from website_categoria")
    marcas = Marca.objects.raw("select * from website_marca")


    try:
        producto = Producto.objects.get(id_producto=pk)
        context = {
            "mensaje": "Editar Producto",
            "grupo": grupo,
            "cat": cat,
            "producto": producto,
        }
        return render(request, "editar.html", context)
    except Producto.DoesNotExist:
        context = {
            "mensaje": "Oferta no encontrada!",
            "grupo": grupo,
            "cat": cat,
        }
        return render(request, "list.html", context)
            "marca": marcas,
            "producto": producto
            }
            return render(request, "editar.html", context)
    except:
            context = {
            "mensaje": "Oferta no encontrada!",
            "grupo": grupo,
            "cat": cat,
            "marca": marcas
            }
            return render(request, "list.html", context)


def Updateproducto(request):
    grupo = "cliente"
    if request.user.groups.filter(name="vendedor").exists():
        grupo = "vendedor"
    elif request.user.groups.filter(name="bodeguero").exists():
        grupo = "bodeguero"
    elif request.user.groups.filter(name="contador").exists():
        grupo = "contador"

    cat = Categoria.objects.all()


    if request.method == "POST":
        id_producto = request.POST.get("id_producto")
        nombre_producto = request.POST.get("nombre")
        precio = request.POST.get("precio")
        descripcion = request.POST.get("descripcion")
        categoria_id = request.POST.get("categoria")

        if not (id_producto and nombre_producto and precio and descripcion and categoria_id):
            return HttpResponseBadRequest("Todos los campos son obligatorios")

        try:
            producto = Producto.objects.get(id_producto=id_producto)
            objCategoria = Categoria.objects.get(id_categoria=categoria_id)

            producto.nombre_producto = nombre_producto
            producto.precio = precio
            producto.descripcion = descripcion
            producto.id_categoria = objCategoria
            producto.save()

            imagen = request.FILES.get("imagen")
            if imagen:
                Imagen_producto.objects.filter(id_producto=producto).delete()
                Imagen_producto.objects.create(
                    imagen_producto=imagen,
                    id_producto=producto
                )

            context = {
                'mensaje': "Se guardaron los cambios hechos en la oferta",
                "grupo": grupo,
                "cat": cat,
                "producto": producto,
            }
            return render(request, 'editar.html', context)

    cat = Categoria.objects.raw("select * from website_categoria")
    marcas = Marca.objects.raw("select * from website_marca")

    if request.method == "POST":
        id_producto = request.POST["id_producto"]
        nombre_producto = request.POST["nombre"]
        precio = request.POST["precio"]
        descripcion = request.POST["descripción"]
        categoria = request.POST["categoria"]
        marcaProd = request.POST["marca"]
        objCategoria = Categoria.objects.get(id_categoria=categoria)
        objMarca = Marca.objects.get(id_marca=marcaProd)

        objProducto = Producto()
        objProducto.id_producto = id_producto
        objProducto.nombre_producto = nombre_producto
        objProducto.precio = precio
        objProducto.descripcion = descripcion
        objProducto.id_categoria = objCategoria
        objProducto.id_marca = objMarca

        imagen = request.FILES.get("imagen")
        Imagen_producto.objects.create(
            imagen_producto=imagen,
            id_producto=objProducto
        )


        except Producto.DoesNotExist:
            context = {
                'mensaje': "Producto no encontrado",
                "grupo": grupo,
                "cat": cat,
            }
            return render(request, 'editar.html', context)
        except Categoria.DoesNotExist:
            context = {
                'mensaje': "Categoría no encontrada",
                "grupo": grupo,
                "cat": cat,
                "producto": producto,
            }
            return render(request, 'editar.html', context)
    else:
        return HttpResponseBadRequest("Método no permitido")
    
def Eliminar(request,pk):
    if request.user.groups.filter(name="vendedor").exists():
        grupo = "vendedor"
    elif request.user.groups.filter(name="bodeguero").exists():
        grupo = "bodeguero"
    elif request.user.groups.filter(name="contador").exists():
        grupo = "contador"
    else:
        grupo = "cliente"

    try:
        producto = Producto.objects.get(id_producto=pk)
        producto.delete()
        mensaje = "Producto Eliminado Correctamente"
        context = {
            "mensaje": mensaje,
            "grupo": grupo,
        }
    except:
        mensaje = "Error, el producto no fue encontrado"
        context = {
            "mensaje": mensaje,
            "grupo": grupo,
        }
    return(redirect("list"))

#SOLO PARA EL USUARIO VENDEDOR
@login_required
def Bodega(request):
    if request.user.groups.filter(name="vendedor").exists():
        grupo = "vendedor"
    elif request.user.groups.filter(name="bodeguero").exists():
        grupo = "bodeguero"
    elif request.user.groups.filter(name="contador").exists():
        grupo = "contador"
    else:
        grupo = "cliente"

    producto = Producto.objects.all().order_by('nombre_producto')
    context = {
        'grupo' : grupo,
        'producto' : producto
    }
    return(render(request,'bodega.html',context,))

#LISTADO DE PRODUCTOS 
@login_required
def List(request):
    if request.user.groups.filter(name="vendedor").exists():
        grupo = "vendedor"
    elif request.user.groups.filter(name="bodeguero").exists():
        grupo = "bodeguero"
    elif request.user.groups.filter(name="contador").exists():
        grupo = "contador"
    else:
        grupo = "cliente"
        
    producto = Producto.objects.all().order_by('nombre_producto')

    #obtener la cantidad de stock de los productos
    stock_disponible = get_productos()
    stock=stock_disponible

    context = {
        'grupo' : grupo,
        'producto' : producto,
        'stock' : stock
    }
    return(render(request,'list.html',context,))

def get_productos():
    url = 'http://localhost/api/api/get.php' 
    r = requests.get(url)
    return r.json()

def Catalogo(request):
    usuario = request.user
    carrito = Carrito.objects.filter(estado=0,usuario=usuario).first()
    contador=Carrito_item.objects.filter(id_carrito=carrito).count()

    if request.user.groups.filter(name="vendedor").exists():
        grupo = "vendedor"
    elif request.user.groups.filter(name="bodeguero").exists():
        grupo = "bodeguero"
    elif request.user.groups.filter(name="contador").exists():
        grupo = "contador"
    else:
        grupo = "cliente"

    #obtener valor del dolar del día
    try:
        dollar_value = get_dollar_value()
    except Exception as e:
        dollar_value = None

    response = requests.get('http://localhost/api/api/get.php')
    product_data = response.json()
    api_product_data = {item['id_producto']: item for item in product_data}

    productos = Producto.objects.all()
    marcas = Marca.objects.all()
    categorias = Categoria.objects.all()

    palabra_clave = request.GET.get('palabra_clave')
    tipo_producto = request.GET.get('tipo_producto')
    marca = request.GET.get('marca')
    precio = request.GET.get('precio')
    stock_disponible = get_productos()
    stock=stock_disponible[0]

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

    # Calcular el precio en dólares de cada producto
    for producto in productos:
        if dollar_value:
            precio_en_dolares = round(producto.precio / dollar_value , 2)
            producto.precio_en_dolares = precio_en_dolares
        else:
            producto.precio_en_dolares = None

        api_data = api_product_data.get(producto.id_producto)
        producto.stock_bodega = api_data['stock_bodega'] if api_data else 0


    context = {     
        "productos": productos,
        "marcas": marcas,
        "categorias" : categorias,
        "contador" : contador,
        "stock" : stock,
        "dollar_value": dollar_value,
        "grupo":grupo
    }   

    return render(request, 'catalogo.html', context)

@login_required
def VerCarrito(request):
    if request.user.groups.filter(name="vendedor").exists():
        grupo = "vendedor"
    elif request.user.groups.filter(name="bodeguero").exists():
        grupo = "bodeguero"
    elif request.user.groups.filter(name="contador").exists():
        grupo = "contador"
    else:
        grupo = "cliente"

    usuario = request.user
    carrito = Carrito.objects.filter(estado=0,usuario=usuario).first()
    carritoItems = Carrito_item.objects.filter(id_carrito = carrito)
    carro = Carrito.objects.filter(usuario=request.user,estado=False).first()
    contCarrito=Carrito_item.objects.filter(id_carrito=carro)
    contador=Carrito_item.objects.filter(id_carrito=carro).count()
    subTotal= sum([item.cantidad* item.id_producto.precio for item in contCarrito])
    total=subTotal+2500

    item = [[9000,'precioenvio','envio',1,2500,"CLP"]]

    for x in carritoItems:
        item.append([
            x.id_producto.id_producto,
            x.id_producto.nombre_producto,
            x.id_producto.descripcion,
            x.cantidad,
            x.id_producto.precio,
            "CLP"
        ])
    items = []

    for x in item:
        items.append({
            "id": x[0],  # El primer elemento de x es el ID del producto
            "title": x[1],  # El segundo elemento de x es el nombre del producto
            "description": x[2],  # El tercer elemento de x es la descripción del producto
            "quantity": x[3],  # El cuarto elemento de x es la cantidad
            "unit_price": x[4],  # El quinto elemento de x es el precio unitario
            "currency_id": x[5]  # El sexto elemento de x es la moneda
        })

    # Creación la preferencia, necesario para Mercado pago
    preference_data = {
        "back_urls": {
            "success": "http://localhost:8000/resultadopago/exito",
            "failure": "http://localhost:8000/resultadopago/fallo",
            "pending": "http://localhost:8000/resultadopago/pendiente"
        }, 
        # En items va la informacion de los productos por lo que se está pagando sta información se saca desde la base de datos 
        "items": items
        # notification_url es para mostrar el resultado de la compra aunque el usuario no vuelva a la página despues de terminar el pago
        # Para probar el notification_url se tiene que usar ngrok
        # "notification_url": "http://localhost:8000/resultadopago/notificacion"
    }

    preference_response = sdk.preference().create(preference_data)
    preference = preference_response["response"]
    print(preference)

    if request.method == 'POST':
        usuario = request.user
        calle = request.POST.get('calle')
        numeracion = request.POST.get('numeracion')
        comuna = request.POST.get('comuna')
        region = request.POST.get('region')
        if Direccion.objects.filter(usuario=request.user) == None:
            Direccion.objects.create(calle=calle,
                                 comuna=comuna,
                                 numeracion=numeracion,
                                 region=region,
                                 usuario=usuario) 

    context={
        'contCarrito':contCarrito,
        'subTotal':subTotal,
        'total':total,
        'carro':carro,
        'contador':contador,
        'url': preference["init_point"],
        "grupo":grupo
    }

    return render(request, 'carrito.html',context )

@login_required
def AñadirCarritoCompra(request):
    if request.method == 'POST':
        usuario=request.user
        id_producto=request.POST['id_producto']
        prod=Producto.objects.filter(id_producto=id_producto).first()
        cantidad=request.POST['cantidad']
        if Carrito.objects.filter(usuario=usuario,estado=False).first() == None:
            Carrito.objects.create(usuario=usuario,estado=False)

        carrito = Carrito.objects.filter(usuario=usuario,estado=False).first()
        if Carrito_item.objects.filter(id_carrito=carrito,id_producto=prod).first():
            carrito_item=Carrito_item.objects.filter(id_carrito=carrito,id_producto=id_producto).first()
            carrito_item.cantidad+=int(cantidad)
            carrito_item.save()
            messages.success(request,'Agregado correctamente')
            return redirect('catalogo')
        else:
            Carrito_item.objects.create(id_carrito=carrito,id_producto=prod,cantidad=cantidad)
            messages.success(request,'Agregado correctamente')
            return redirect('catalogo')

    return render(request,'catalogo.html') 

@login_required
def ActualizarCantidadCarrito(request):
    if request.method=='POST':
        usuario=request.user
        car= request.POST.get('id_carrito')
        cantidad= request.POST.get('cantidad')
        prod = request.POST.get('id_producto')
        carItem=Carrito_item.objects.filter(id_carrito=car,id_producto=prod).first()
        carItem.cantidad=cantidad
        carItem.save()
        return redirect('VerCarrito')
    return render(request,'mainCarrito.html')

@login_required
def QuitarCarritoCompra(request):
    if request.method == 'POST':
        usuario=request.user
        carrito = Carrito.objects.filter(usuario=usuario,estado=False)
        if request.POST.get('borrarUno'):
            id_producto=request.POST['id_producto']
            id_carrito=request.POST['id_carrito']
            carrito_item = Carrito_item.objects.filter(id_carrito=id_carrito,id_producto=id_producto)
            carrito_item.delete()
            messages.success(request,'Eliminado correctamente')
            return redirect('VerCarrito')        
        elif request.POST.get('borrarTodo'):
            carrito.delete()
            Carrito.objects.create(estado=False,usuario=usuario)
            messages.success(request,'Eliminado Correctamente')
            return redirect('VerCarrito')
    return render(request,'mainCarrito.html')

def ResultadoPago(request,rp):
    context={
        'rp':rp,

    }
    usuario = request.user
    carritoAntiguo = Carrito.objects.filter(usuario=usuario,estado=0).first()
    estados=Estado.objects.get(nombre='Pendiente')

    carro = Carrito.objects.filter(usuario=request.user,estado=False).first()
    contCarrito=Carrito_item.objects.filter(id_carrito=carro)

    if rp == "exito":
        carritoAntiguo.estado=1
        carritoAntiguo.save()
        Carrito.objects.create(estado=0,usuario=usuario)
        Pedido.objects.create(id_carrito=carritoAntiguo,usuario=usuario,id_envio=estados)
        for producto in contCarrito:
            # Se obtiene el stock actal del producto en la API
            stock = requests.get('http://localhost/api/api/get_one.php', json={"id_producto": producto.id_producto.id_producto}).json().get('stock_bodega')
            # Se le resta al stock actual la cantidad de productos comprados
            stock = stock - producto.cantidad
            # se actualiza el stock en la API
            requests.put('http://localhost/api/api/put.php',
                          json={
                            "id_producto": producto.id_producto.id_producto,
                            "nombre_producto": producto.id_producto.nombre_producto,
                            "precio": producto.id_producto.precio,
                            "descripcion": producto.id_producto.descripcion,
                            "stock_bodega": stock,
                            "id_marca": producto.id_producto.id_marca.id_marca,
                            "id_categoria": producto.id_producto.id_categoria.id_categoria
                            })
    return render(request, 'resultadopago.html',context)

def Detalle(request,id_producto):
    producto = get_object_or_404(Producto, id_producto=id_producto)
    usuario = request.user
    carrito = Carrito.objects.filter(estado=False,usuario=usuario).first()
    contador=Carrito_item.objects.filter(id_carrito=carrito).count()
    stock = requests.get('http://localhost/api/api/get_one.php', json={"id_producto": id_producto}).json().get('stock_bodega')
    try:
        dollar_value = get_dollar_value()
    except Exception as e:
        dollar_value = None

    if dollar_value:
        precio_en_dolares = round(producto.precio / dollar_value , 2)
        producto.precio_en_dolares = precio_en_dolares
    else:
        producto.precio_en_dolares = None

    context= {
        'producto':producto,
        'contador':contador,
        'stock':stock,
        "dollar_value":dollar_value
    }

    return render(request, 'detalle.html',context)

def quienesSomos(request):
    if request.user.groups.filter(name="vendedor").exists():
        grupo = "vendedor"
    elif request.user.groups.filter(name="bodeguero").exists():
        grupo = "bodeguero"
    elif request.user.groups.filter(name="contador").exists():
        grupo = "contador"
    else:
        grupo = "cliente"

    context ={
        "grupo":grupo
    }
    return render(request,'quienesSomos.html',context)

def Cuenta(request):
    if request.user.groups.filter(name="vendedor").exists():
        grupo = "vendedor"
    elif request.user.groups.filter(name="bodeguero").exists():
        grupo = "bodeguero"
    elif request.user.groups.filter(name="contador").exists():
        grupo = "contador"
    else:
        grupo = "cliente"
    usuario = request.user
    pedidos = Pedido.objects.filter(usuario=usuario)
    carritos = Carrito.objects.filter(usuario=usuario,estado=1)
    items = Carrito_item.objects.all()
    context = {
        'pedidos':pedidos,
        'carritos':carritos,
        'items':items,
        "grupo":grupo
    }

    return render(request,'cuenta.html',context)

def contacto(request):
    if request.user.groups.filter(name="vendedor").exists():
        grupo = "vendedor"
    elif request.user.groups.filter(name="bodeguero").exists():
        grupo = "bodeguero"
    elif request.user.groups.filter(name="contador").exists():
        grupo = "contador"
    else:
        grupo = "cliente"

    context ={
        "grupo":grupo
    }
    return render(request,'contacto.html',context)  

class PedidoFiltro(django_filters.FilterSet): 

    class Meta:
        model = Pedido
        fields = ['usuario','fecha','id_envio']

def prepararPedido(request):

    if request.user.groups.filter(name="vendedor").exists():
        grupo = "vendedor"
    elif request.user.groups.filter(name="bodeguero").exists():
        grupo = "bodeguero"
    elif request.user.groups.filter(name="contador").exists():
        grupo = "contador"
    else:
        grupo = "cliente"

    pedidos = Pedido.objects.all()
    carro = Carrito.objects.filter(usuario=request.user,estado=False).first()
    contador=Carrito_item.objects.filter(id_carrito=carro).count()
    filtro = PedidoFiltro(request.GET, queryset=pedidos)
    pedidos = filtro.qs
    estados = Estado.objects.all()
    direcciones = Direccion.objects.all()

    if request.method == 'POST'  :
        estado_op = request.POST.get('estadoOp')
        estado = Estado.objects.get(nombre=estado_op)
        Pedido.objects.filter(id_pedido=request.POST.get('idpedido')).update(id_envio=estado)

    context = {
        'pedidos':pedidos,
        'contador':contador,
        'filtro':filtro,
        'estados':estados,
        'direcciones':direcciones,
        "grupo":grupo
    }
    return render(request,'prepararPedido.html',context)  

def grafico(data, labels):
    plt.figure(figsize=(6, 6))
    plt.pie(data, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal') 
    
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')
    
    return graphic

def finanzas(request):
    productos = Producto.objects.all()
    mercaderias = sum(producto.precio * producto.cant_inventario for producto in productos) * 0.8
    pedidos = Pedido.objects.all()
    ventas = sum(pedido.total for pedido in pedidos)
    impuestos = ventas*0.19
    inmuebles = 1200000
    remuneraciones = 8000000
    proveedores= mercaderias*0.8
    capital = 3000000
    activos = mercaderias + inmuebles
    pasivos = ventas+impuestos+remuneraciones+proveedores

    data = [capital, activos, pasivos]
    labels = ['Capital', 'Activos', 'Pasivos']

    graficoTorta = grafico(data, labels)

    context = {
        'mercaderias' : mercaderias, 
        'ventas' : ventas,
        'impuestos' : impuestos,
        'remuneraciones' : remuneraciones,
        'proveedores' : proveedores,
        'capital':capital,
        'inmuebles':inmuebles,
        'activos':activos,
        'pasivos':pasivos,
        'graficoTorta':graficoTorta
    }

    return render(request, 'finanzas.html', context)
