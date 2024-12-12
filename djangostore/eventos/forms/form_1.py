from django import forms
from ..models import Evento
from django.utils.safestring import mark_safe

OPCIONES_COMIDAS = [ 
    (1,'Yes'),
    (0,'No'),
]

# Formulario del evento 1 **********************************************************************************************************************
class PrecioFormEvento1(forms.Form):
    __student = 100
    __standard  = 200

    OPCIONES_PRECIOS = [
        (__student, f'Student - {__student} €'),
        (__standard, f'Standard - {__standard} €'),
    ]

    precioModality = forms.ChoiceField(
        widget = forms.RadioSelect,
        choices = OPCIONES_PRECIOS, 
        initial = __standard,
        label = "Please select the corresponding option:"
    )

    precioFinal = forms.IntegerField(
        required = False, 
        label = 'Price:', 
        initial = __standard,
        widget = forms.NumberInput(attrs={
            'class': 'precio-final',
            'disabled': 'disabled'
        }),        
    )
