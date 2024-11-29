from django import forms
from .models import Evento

class CambiarPrecioFormEvento1(forms.ModelForm):
    OPCIONES_PRECIOS = [
        (100, 'Student'),
        (200, 'Standard'),
    ]

    precio = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=OPCIONES_PRECIOS, 
        label="Modality"
    )
    
    class Meta:
        model = Evento
        fields = ['precio']

class CambiarPrecioFormEvento2(forms.ModelForm):
    OPCIONES_PRECIOS = [
        (220, 'Student'),
        (550, 'Normal'),
    ]

    precio = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=OPCIONES_PRECIOS, 
        label="Modality"
    )

    class Meta:
        model = Evento
        fields = ['precio']