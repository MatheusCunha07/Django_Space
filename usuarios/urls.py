from django.urls import path
from usuarios.views import login, cadastro, logout

urlpatterns = [
    path('login', login, name='login'),  # Home page of the galeria app
    path('cadastro', cadastro, name='cadastro'),  # Home page of the galeria app
    path('logout', logout, name='logout'),  # Default route to login
]