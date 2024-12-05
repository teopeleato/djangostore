from django import forms
from .models import Evento

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

    precioModality = forms.ChoiceField(
        widget = forms.RadioSelect,
        choices = OPCIONES_PRECIOS, 
        initial = __standard,
        label = "Please select the corresponding option:"
    )    

    precioFinal = forms.IntegerField(
        required = False, 
        label = 'Amount to pay:', 
        initial = __standard,
        widget = forms.NumberInput(attrs={
            'class': 'precio-final',
            'disabled': 'disabled'
        }),        
    )
    