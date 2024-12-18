from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Evento
from .forms import PrecioFormEvento
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
    # Obtener el evento a partir del código
    evento = get_object_or_404(Evento,codigo_i3a=codigo_i3a)

    if request.method == "POST":

        # Solo procesamos el nuevo precio enviado por AJAX
        nuevo_precio = request.POST.get('nuevoPrecio')

        # Procesar el precio o realizar cualquier cálculo que necesites (si es necesario)
        # Aquí solo devolvemos el precio recibido, en caso de que quieras realizar validaciones adicionales, puedes agregarlas aquí

        return JsonResponse({
            'mensaje': 'Precio recibido correctamente',
            'nuevoPrecio': nuevo_precio
        })
    
  

        

    else:

        # Lógica para seleccionar formulario según el evento, con solicitudes GET normales    
        PrecioForm = PrecioFormEvento

        # Cargo el evento con su formulario
        form = PrecioForm(codigo_i3a=evento.codigo_i3a) 
        return render(request, 'eventos/detalle_evento.html', {
            'evento': evento, 
            'form': form
        }) 
