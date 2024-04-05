from django.urls import path
from .views import * # no olvidar agregar msg para las notificaciones despues
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('base',Base,name='base'), 
    path('login',Login,name='login'),
    path('register',Register,name='register'),
    path('',Landing,name='landing'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)