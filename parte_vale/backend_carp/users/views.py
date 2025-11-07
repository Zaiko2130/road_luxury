from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken
from django.views import View
from django.shortcuts import render, redirect


# --- API ENDPOINTS (PARA REACT / POSTMAN / ANDROID) ---

class RegisterView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if User.objects.filter(username=username).exists():
            return Response({"error": "El usuario ya existe"}, status=status.HTTP_400_BAD_REQUEST)

        User.objects.create_user(username=username, password=password)
        return Response({"message": "Usuario creado con éxito"}, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user is None:
            return Response({"error": "Credenciales inválidas"}, status=status.HTTP_400_BAD_REQUEST)

        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }, status=status.HTTP_200_OK)


# --- LOGIN PARA LA WEB (HTML) ---

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            # Redirige a la página del catálogo después de iniciar sesión
            return redirect("catalogo")  # Asegúrate que esta URL exista en urls.py
        else:
            return render(request, "login.html", {"error": "Usuario o contraseña incorrectos"})

    return render(request, "login.html")


# --- REGISTRO PARA LA WEB (HTML) ---

class RegisterPageView(View):
    def get(self, request):
        return render(request, 'registro.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if not username or not password:
            return render(request, 'registro.html', {'error': 'Usuario y contraseña son obligatorios'})

        if User.objects.filter(username=username).exists():
            return render(request, 'registro.html', {'error': 'El usuario ya existe'})

        # Crear el usuario con email opcional
        User.objects.create_user(username=username, password=password, email=email)

        # Luego de registrarse, redirige directamente al catálogo o al login si prefieres
        return redirect('catalogo')  # Cambia a 'login' si quieres que primero inicie sesión


# --- VISTA PARA EL CATÁLOGO ---

def catalogo_view(request):
    # Aquí podrías agregar lógica para pasar datos de vehículos al template
    # Por ahora simplemente renderiza el template catalogo.html
    return render(request, 'catalogo.html')
