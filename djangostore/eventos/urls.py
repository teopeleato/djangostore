from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    # path('lista-eventos', views.lista_eventos, name='lista_eventos'),
    path('<int:codigo_i3a>', views.detalle_evento, name='detalle_evento'),
    # path('<int:codigo_i3a>/actualizar_precio/', views.actualizar_precio, name='actualizar_precio'),
]
