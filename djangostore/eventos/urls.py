from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    # path('lista-eventos', views.lista_eventos, name='lista_eventos'),
    path('<str:titulo>', views.detalle_evento, name='detalle_evento'),
]
