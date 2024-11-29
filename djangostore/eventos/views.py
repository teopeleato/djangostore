from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Evento
from .forms import CambiarPrecioFormEvento1, CambiarPrecioFormEvento2
from django.views.decorators.csrf import csrf_exempt
import logging

logger = logging.getLogger(__name__)


def home(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/home.html', {'eventos': eventos})

'''
def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos})
'''

def detalle_evento(request, codigo_i3a):
    evento = get_object_or_404(Evento,codigo_i3a=codigo_i3a)

    # Lógica para seleccionar formulario según el evento
    if evento.codigo_i3a == 1:
        CambiarPrecioForm = CambiarPrecioFormEvento1
    if evento.codigo_i3a == 2:
        CambiarPrecioForm = CambiarPrecioFormEvento2

    if request.method == 'POST':
        form = CambiarPrecioForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('detalle_evento', codigo_i3a=evento.codigo_i3a)
    else:
        form = CambiarPrecioForm(instance=evento)

    return render(request, 'eventos/detalle_evento.html', {'evento': evento, 'form': form})

'''
def actualizar_precio(request, codigo_i3a):
    if request.method == 'POST' and request.is_ajax():
        nuevo_precio = request.POST.get('precio')
        evento = get_object_or_404(Evento, codigo_i3a=codigo_i3a)
        evento.precio = nuevo_precio
        evento.save()

        # Respuesta en JSON
        return JsonResponse({'status': 'success', 'nuevo_precio': evento.precio})

    return JsonResponse({'status': 'error'}, status=400)
'''

def es_ajax(request):
    return request.headers.get('X-Requested-With') == 'XMLHttpRequest'

def actualizar_precio(request, codigo_i3a):
    if request.method == 'POST' and es_ajax(request):
        logger.info("Solicitud AJAX válida")
        nuevo_precio = request.POST.get('precio')
        logger.info(f"Precio recibido: {nuevo_precio}")

        if not nuevo_precio:
            logger.error("No se envió un precio válido")
            return JsonResponse({'status': 'error', 'message': 'Precio no enviado'}, status=400)

        
        try:
            nuevo_precio = int(nuevo_precio)  # Asegúrate de que sea un entero
            evento = get_object_or_404(Evento, codigo_i3a=codigo_i3a)
            evento.precio = nuevo_precio  
            evento.save()
            logger.info(f"Precio actualizado a: {evento.precio}")
            return JsonResponse({'status': 'success', 'nuevo_precio': evento.precio})
        except (ValueError, TypeError) as e:
            logger.error(f"Error al convertir el precio: {e}")
            return JsonResponse({'status': 'error', 'message': 'Precio no válido'}, status=400)

    logger.error("Solicitud inválida")
    return JsonResponse({'status': 'error', 'message': 'Solicitud inválida'}, status=400)