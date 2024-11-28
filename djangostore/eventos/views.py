from django.shortcuts import render
from .models import Evento

def home(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/home.html', {'eventos': eventos})

'''
def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos})
'''