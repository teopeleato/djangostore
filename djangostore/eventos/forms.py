from django import forms
from .models import Evento

# Formulario del evento 1 ***********************************************************
class PrecioFormEvento1(forms.Form):
    __student = 100
    __standard  = 200
    OPCIONES_PRECIOS = [
        (__student, 'Student'),
        (__standard, 'Standard'),
    ]

    precioModality = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=OPCIONES_PRECIOS, 
        label="Modality"
    )

    precioFinal = forms.IntegerField(required=False, label='Price', initial=0)


# Formulario del evento 2 ***********************************************************
class PrecioFormEvento2(forms.Form):
    OPCIONES_PRECIOS = [
        (220, 'Student'),
        (550, 'Normal'),
    ]

    precioModality = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=OPCIONES_PRECIOS, 
        label="Modality"
    )

    precioFinal = forms.IntegerField(required=False, label='Price', initial=0)
