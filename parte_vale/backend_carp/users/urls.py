from django.urls import path
from .views import login_page, RegisterPageView, RegisterView, LoginView, catalogo_view

urlpatterns = [
    path('login/', login_page, name='login'),          # vista login HTML
    path('register/', RegisterPageView.as_view(), name='register'),  # vista registro HTML
    path('api-register/', RegisterView.as_view(), name='api-register'),  # API register (POST)
    path('api-login/', LoginView.as_view(), name='api-login'),           # API login (POST)
    path('catalogo/', catalogo_view, name='catalogo'),  # ruta para mostrar el catálogo
]
