from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ruta para la página principal
    # path('lista-eventos', views.lista_eventos, name='lista_eventos'),
]
