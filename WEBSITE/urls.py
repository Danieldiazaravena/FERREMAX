from django.urls import path
from .views import * # no olvidar agregar msg para las notificaciones despues
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('base',Base,name='base'), 
    path('woi',Woi,name='woi'), 
    path('accounts/register',Register,name='register'),
    path('',Landing,name='landing'),
    path('agregar/', Agregar, name='agregar'),
    path('catalogo/', Catalogo, name='catalogo'),
    path('carrito/',VerCarrito,name='VerCarrito'),
    path('carrito/add',AñadirCarritoCompra,name='AñadirCarritoCompra'),
    path('carrito/upd',ActualizarCantidadCarrito, name="ActualizarCantidadCarrito"),
    path('carrito/del',QuitarCarritoCompra,name='QuitarCarritoCompra'),
    path('resultadopago/<str:rp>',ResultadoPago,name='Resultadopago'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
