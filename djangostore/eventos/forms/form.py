from django import forms
from django.utils.safestring import mark_safe
import os
import json


class PrecioFormEvento(forms.Form):
    # Constructor
    def __init__(self, codigo_i3a=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Cargar datos desde el JSON
        data = self.load_json_data()
        evento = self.get_event_data(data, codigo_i3a)

        # Configurar campos dinámicos
        self.configure_dynamic_fields(evento)

    def load_json_data(self):
        """Carga los datos del archivo JSON."""
        json_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../static/files/options.json'))
        try:
            with open(json_file_path, 'r') as f:
                data = json.load(f)
                if not isinstance(data, dict):
                    raise ValueError("El archivo JSON no tiene el formato esperado.")
                return data
        except FileNotFoundError:
            print(f"ERROR - No se encontró el archivo JSON en: {json_file_path}")
            return {"eventos": []}
        except ValueError as e:
            print(f"ERROR - Problema al cargar el archivo JSON: {e}")
            return {"eventos": []}

    def get_event_data(self, data, codigo_i3a):
        """Obtiene los datos del evento según el código."""
        print(f"DEBUG - Valor de codigo_i3a: {codigo_i3a}")
        return next((evento for evento in data.get("eventos", []) if evento["codigo_i3a"] == codigo_i3a), None)

    def configure_dynamic_fields(self, evento):

        opciones_social= [ 
            (1,'Yes'),
            (0,'No'),
        ]
        
        """Configura los campos dinámicos según los datos del evento."""
        if evento:
            print(f"DEBUG - Evento seleccionado: {evento}")
            precio_inicial = evento.get("precio_inicial")
            opciones_precios = [(item['value'], item['label']) for item in evento.get("precios", [])]
            social_1 = evento.get("social_1")
            social_2 = evento.get("social_2")
        else:
            print(f"ERROR - No se encontró un evento con el código especificado.")
            opciones_precios = []

        # Configurar campos dinámicos
        self.fields['precioModality'] = forms.ChoiceField(
            widget=forms.RadioSelect(),
            choices=opciones_precios,
            initial=precio_inicial,
            label="Modality:"
        )

        self.fields['papers'] = forms.CharField(
            required=False,
            label="If you present paper/s, tell us the number ID of it or them:",
        )

        if social_1:
            self.fields['social_1'] = forms.ChoiceField(
                widget=forms.RadioSelect(),
                initial=0,
                choices=opciones_social,
                label=social_1
            )

        if social_2:
            self.fields['social_2'] = forms.ChoiceField(
                widget=forms.RadioSelect(),
                initial=0,
                choices=opciones_social,
                label=social_2
            )        

        self.fields['intolerancias'] = forms.CharField(
            required=False,
            widget=forms.Textarea(attrs={
                'rows':3, 
                'cols':35,
            }),
            label="Tell us if you want a vegan or vegetarian menu. And if you have any food allergy or intolerance:",
         )

        self.fields['precioFinal'] = forms.IntegerField(
            required=False,
            label=mark_safe('Total to pay in &#8364;:'),
            initial=precio_inicial,
            widget=forms.NumberInput(attrs={
                'class': 'precio-final',
                'disabled': 'disabled',
                'readonly': 'readonly'
            }),
        )