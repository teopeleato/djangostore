from django import forms
from .models import Evento
from django.utils.safestring import mark_safe

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

# Formulario del evento 2 **********************************************************************************************************************
class PrecioFormEvento2(forms.Form):
    __student = 350
    __standard  = 580

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

# Formulario del evento 3 **********************************************************************************************************************
class PrecioFormEvento3(forms.Form):
    __student = 90
    __standard  = 500

    # Descuento a members
    __descuento_member = 10
    __student_and_member = __student * (100-__descuento_member)/100
    __standard_and_member = __standard * (100-__descuento_member)/100
    __student_and_member = round(__student_and_member)
    __standard_and_member = round(__standard_and_member)

    OPCIONES_PRECIOS = [
        (__student, f'Student - {__student} €'),
        (__standard, f'Standard - {__standard} €'),
        (__student_and_member, f'Student and member - {__student_and_member} € (-{__descuento_member}% inc.)'),
        (__standard_and_member, f'Standard and member - {__standard_and_member} € (-{__descuento_member}% inc.)'),
    ]

    # Campos que definen el precio

    precioModality = forms.ChoiceField(
        widget = forms.RadioSelect(attrs={
            'class': 'p-3',
        }),
        choices = OPCIONES_PRECIOS, 
        initial = __standard,
        label = "Please select the corresponding option:",          
    )  

    # Campos que no influyen en el precio, informativos

    texto_informativo = forms.CharField(
        initial="Please mark your optional options:",
        required=False,
        widget=forms.TextInput(attrs={
            'readonly': 'readonly',  # Hace que el campo no sea editable
            'class': 'form-control-plaintext',
        }),
        label="",
    )

    comida = forms.BooleanField(
        required = False,  
        label = "Lunch 5 June", 
        widget = forms.CheckboxInput(attrs={
            'class': 'check-opcionales',
        }),
    )  

    cena = forms.BooleanField(
        widget = forms.CheckboxInput(attrs={
            'class': 'check-opcionales',
        }),
        required = False,  
        label = "Dinner 5 June",         
    )

    # Precio final

    precioFinal = forms.IntegerField(
        required = False, 
        label=mark_safe('Amount to pay in &#8364;:'),  # Marca el label como HTML seguro
        initial = __standard,
        widget = forms.NumberInput(attrs={
            'class': 'precio-final',
            'disabled': 'disabled',
            'readonly': 'readonly'
        }),        
    )
    