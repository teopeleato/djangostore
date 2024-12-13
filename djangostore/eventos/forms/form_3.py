from django import forms
from ..models import Evento
from django.utils.safestring import mark_safe

OPCIONES_COMIDAS = [ 
    (1,'Yes'),
    (0,'No'),
]

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

    # Campos que definen el precio ************************************************************************************************************************

    precioModality = forms.ChoiceField(
        widget = forms.RadioSelect(),
        choices = OPCIONES_PRECIOS, 
        initial = __standard,
        label = "Modality:",          
    )  

    # Campos que no influyen en el precio, informativos ************************************************************

    """ texto_informativo = forms.CharField(
        initial="Please mark your optional options:",
        required=False,
        widget=forms.TextInput(attrs={
            'readonly': 'readonly',  # Hace que el campo no sea editable
            'class': 'form-control-plaintext',
        }),
        label="",
    ) """

    papers = forms.CharField(
        required=False,
        label="If you present paper/s, tell us the number ID of it or them:",
    )

    """ comida = forms.BooleanField(
        required = False,  
        widget = forms.CheckboxInput(attrs={
            'class': 'check-opcionales',
        }),
        label = "Lunch 5 June", 
    )  
 """

    comida = forms.ChoiceField(
        widget = forms.RadioSelect(),
        initial = 0,        
        choices = OPCIONES_COMIDAS, 
        label = "Are you attending the lunch on 5 June?", 
    )

    cena = forms.ChoiceField(
        widget = forms.RadioSelect(),
        initial = 0,        
        choices = OPCIONES_COMIDAS, 
        label = "Are you attending the dinner on 6 June?", 
    )

    intolerancias = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'rows':3, 
            'cols':35,
        }),
        label="Tell us if you want a vegan or vegetarian menu. And if you have any food allergy or intolerance:",
    )

    # Precio final ************************************************************************************************************************

    precioFinal = forms.IntegerField(
        required = False, 
        label=mark_safe('Total to pay in &#8364;:'),  # Marca el label como HTML seguro
        initial = __standard,
        widget = forms.NumberInput(attrs={
            'class': 'precio-final',
            'disabled': 'disabled',
            'readonly': 'readonly'
        }),        
    )
    