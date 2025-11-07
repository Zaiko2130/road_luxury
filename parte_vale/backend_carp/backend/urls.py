from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

urlpatterns = [
    path('', home, name='home'),  
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # Aquí incluyes las URLs de la app usuarios (login, register)
    path('catalogo/', lambda request: render(request, 'catalogo.html'), name='catalogo'),  # Ruta ejemplo para catálogo
]
