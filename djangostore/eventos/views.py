from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Evento
from .forms import PrecioFormEvento1, PrecioFormEvento2, PrecioFormEvento3
from django.views.decorators.csrf import csrf_exempt
import logging

logger = logging.getLogger(__name__)

def home(request):
    eventos = Evento.objects.filter(activo=True)
    return render(request, 'eventos/home.html', {'eventos': eventos})

'''
def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos})
'''

def detalle_evento(request, codigo_i3a):
    evento = get_object_or_404(Evento,codigo_i3a=codigo_i3a)

    if request.method == "POST":
        # Recojo el valor nuevoPrecio del data enviado por ajax
        nuevo_precio = request.POST.get('nuevoPrecio')  
        # print(f"Nuevo precio recibido: {nuevo_precio}")

        # Devolver la respuesta JSON para actualizar el precio en el cliente
        return JsonResponse({
            'mensaje': 'Precio recibido correctamente', 
            'nuevoPrecio': nuevo_precio
        })

    # Lógica para seleccionar formulario según el evento, con solicitudes GET normales
    if evento.codigo_i3a == 1:
        PrecioForm = PrecioFormEvento1
    if evento.codigo_i3a == 2:
        PrecioForm = PrecioFormEvento2
    if evento.codigo_i3a == 3:
        PrecioForm = PrecioFormEvento3

    # Cargo el evento con su formulario
    form = PrecioForm() 
    return render(request, 'eventos/detalle_evento.html', {
        'evento': evento, 
        'form': form
    }) 
