from django.urls import path
from galeria.views import index, imagem, buscar

urlpatterns = [
    path('', index, name='index'), # Home page of the galeria app
    path('imagem/<int:foto_id>', imagem, name='imagem'), # Image detail page
    path('buscar', buscar, name='buscar'), 
]
