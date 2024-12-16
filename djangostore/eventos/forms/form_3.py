from django import forms
from ..models import Evento
from django.utils.safestring import mark_safe
import os
import json

class PrecioFormEvento3(forms.Form):

    # Obtener la ruta de la carpeta que contiene el archivo forms.py
    forms_dir = os.path.dirname(os.path.abspath(__file__))  # Carpeta 'forms'
       
    
    # Ruta relativa al archivo JSON desde el archivo actual
    json_file_path = os.path.join(os.path.dirname(__file__), '../static/files/options.json')

    # Normaliza y convierte a absoluta
    json_file_path = os.path.abspath(json_file_path)

    # print(f"DEBUG - Valor de json_file_path: {json_file_path}")
    
    try:
        # Cargar datos del JSON
        with open(json_file_path, 'r') as f:
            data = json.load(f)
            print(f"DEBUG - Contenido del archivo JSON: {data}")
    except FileNotFoundError:
        print(f"ERROR - No se encontró el archivo JSON en: {json_file_path}")
        data = {"eventos": []}

    #OPCIONES_COMIDAS = [(item['value'], item['label']) for item in data.get('comidas', [])]
    #OPCIONES_PRECIOS = [(item['value'], item['label']) for item in data.get('precios', [])]

    # Definir el valor inicial para 'precioModality' desde el JSON
    #precio_inicial = data.get('precio_inicial')
    #print(f"DEBUG - Valor de precio_inicial: {precio_inicial}")

    # Código del evento deseado
    #codigo_evento_deseado = 3  
    print(f"DEBUG - Valor de Evento.codigo_i3a: {Evento.codigo_i3a}")


    # Filtrar el evento con el código correspondiente
    evento = next((evento for evento in data.get("eventos", []) if evento["codigo_evento"] == Evento.codigo_i3a), None)

    if evento:
        print(f"DEBUG - Evento seleccionado: {evento}")
        precio_inicial = evento.get("precio_inicial", 500)
        OPCIONES_PRECIOS = [(item['value'], item['label']) for item in evento.get("precios", [])]
        OPCIONES_COMIDAS = [(item['value'], item['label']) for item in evento.get("comidas", [])]
    else:
        print(f"ERROR - No se encontró un evento con codigo_evento=")
        precio_inicial = 500
        OPCIONES_PRECIOS = []
        OPCIONES_COMIDAS = []

    '''
    OPCIONES_COMIDAS = [ 
    (1,'Yes'),
    (0,'No'),
]
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
    '''
    


    # Campos que definen el precio ************************************************************************************************************************

    """ precioModality = forms.ChoiceField(
        widget = forms.RadioSelect(),
        choices = OPCIONES_PRECIOS, 
        initial = __standard,
        label = "Modality:",          
    )  """ 
    precioModality = forms.ChoiceField(
        widget = forms.RadioSelect(),
        choices = OPCIONES_PRECIOS, 
        initial=precio_inicial,  
        label = "Modality:",          
    )

    # Campos que no influyen en el precio, informativos ************************************************************

    papers = forms.CharField(
        required=False,
        label="If you present paper/s, tell us the number ID of it or them:",
    )

    

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
        # initial = __standard,
        initial=precio_inicial,
        widget = forms.NumberInput(attrs={
            'class': 'precio-final',
            'disabled': 'disabled',
            'readonly': 'readonly'
        }),        
    )
    