from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Evento
from .forms import PrecioFormEvento1, PrecioFormEvento2
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
        PrecioForm = PrecioFormEvento1
    if evento.codigo_i3a == 2:
        PrecioForm = PrecioFormEvento2

    if request.method == 'POST':
        form = PrecioForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('detalle_evento', codigo_i3a=evento.codigo_i3a)
    else:
        form = PrecioForm() 
    return render(request, 'eventos/detalle_evento.html', {'evento': evento, 'form': form})
