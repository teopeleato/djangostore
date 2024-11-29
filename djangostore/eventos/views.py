from django.shortcuts import render, get_object_or_404, redirect
from .models import Evento
from .forms import CambiarPrecioFormEvento1, CambiarPrecioFormEvento2

def home(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/home.html', {'eventos': eventos})

'''
def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos})
'''

def detalle_evento(request, titulo):
    evento = get_object_or_404(Evento,titulo=titulo)

    # Lógica para seleccionar formulario según el evento
    if evento.codigo_i3a == 1:
        CambiarPrecioForm = CambiarPrecioFormEvento1
    if evento.codigo_i3a == 2:
        CambiarPrecioForm = CambiarPrecioFormEvento2

    if request.method == 'POST':
        form = CambiarPrecioForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('detalle_evento', titulo=evento.titulo)
    else:
        form = CambiarPrecioForm(instance=evento)

    return render(request, 'eventos/detalle_evento.html', {'evento': evento, 'form': form})


    #return render(request, "eventos/detalle_evento.html", {"evento":evento})