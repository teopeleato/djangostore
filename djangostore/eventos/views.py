from django.shortcuts import render
from .models import Evento

def home(request):
    return render(request, 'home.html')

def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos})
