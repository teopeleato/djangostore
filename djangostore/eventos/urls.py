from django.urls import path
from . import views

urlpatterns = [
    # Ruta inicial que llama a la vista `lista_eventos`
    path('', views.lista_eventos, name='lista_eventos'),
]
