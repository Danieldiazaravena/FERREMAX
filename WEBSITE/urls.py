from django.urls import path
from .views import * # no olvidar agregar msg para las notificaciones despues
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
<<<<<<< HEAD
    path('login',Login,name='login'),
    path('register',Register,name='register'),
    path('',Landing,name='landing'),
    path('404',Woi,name='woi'), 
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
=======
    path('base',Base,name='base'), 
    path('accounts/register',Register,name='register'),
    path('',Landing,name='landing'),
    path('agregar/', Agregar, name='agregar'),
    path('catalogo/', Catalogo, name='catalogo'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 756924f3d7b5b9b839217d0aa57fcf5fad41e17f
