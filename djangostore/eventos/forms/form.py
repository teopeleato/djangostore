from django import forms
from django.utils.safestring import mark_safe
import os
import json


class PrecioFormEvento(forms.Form):

    # Mapear widgets del JSON a widgets de Django
    WIDGET_MAPPING = {
        "textarea": forms.Textarea(attrs={'rows': 3, 'cols': 35}),
        "textinput": forms.TextInput(),
        "emailinput": forms.EmailInput(),
    }

    # Constructor
    def __init__(self, codigo_i3a=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Cargar datos desde el JSON
        data = self.load_json_data()
        evento = self.get_event_data(data, codigo_i3a)

        # Configurar campos dinámicos
        self.configure_dynamic_fields(evento)

        # Agregar un asterisco rojo a los campos requeridos
        self.add_required_asterisk()

    def load_json_data(self):
        # Carga los datos del archivo JSON
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

    # Obtener los datos del evento según el código
    def get_event_data(self, data, codigo_i3a):
        # print(f"DEBUG - Valor de codigo_i3a: {codigo_i3a}")
        return next((evento for evento in data.get("eventos", []) if evento["codigo_i3a"] == codigo_i3a), None)

    def configure_dynamic_fields(self, evento):

        opciones_social= [ 
            (1,'Yes'),
            (0,'No'),
        ]
        
        # Configurar campos dinámicos
        if evento:
            # print(f"DEBUG - Evento seleccionado: {evento}")
            precio_inicial = evento.get("precio_inicial")
            opciones_precios = [(item['value'], item['label']) for item in evento.get("precios", [])]
            campos = evento.get("campos", [])
        else:
            print(f"ERROR - No se encontró un evento con el código especificado.")
            precio_inicial = 0
            opciones_precios = []
            campos = []
               
        # Crear dinámicamente los campos sociales según el tipo definido en el JSON
        for campo in campos:

            # Configurar el campo de precios
            if "precios" in campo:
                opciones_precios = [(item['value'], item['label']) for item in campo["precios"]]
                self.fields['precioModality'] = forms.ChoiceField(
                    widget=forms.RadioSelect(),
                    choices=opciones_precios,
                    label="Select a pricing option"
                )

            # Crear dinámicamente los campos
            else:
                field_name = campo['name']  # Nombre del campo
                field_label = campo['label']  # Etiqueta del campo
                field_type = campo['type']  # Tipo de campo
                widget_key = campo.get('widget', 'textinput')  # Widget con Valor predeterminado
                field_required = campo.get('required', False) == 'True' # Obligatoriedad. Si 'required' es 'True', se asignará True; de lo contrario, se asignará False.

                # Obtener el widget del diccionario de mapeo
                widget = self.WIDGET_MAPPING.get(widget_key, forms.TextInput())

                if field_type == "ChoiceField":
                    opciones = campo.get("choices", [(1, "Yes"), (0, "No")])  # Valores predeterminados
                    self.fields[field_name] = forms.ChoiceField(
                        widget=forms.RadioSelect(),
                        required=field_required,
                        choices=opciones,
                        label=field_label
                    )
                elif field_type == "CharField":
                    self.fields[field_name] = forms.CharField(
                        required=field_required,
                        label=field_label,
                        widget=widget
                    )
                elif field_type == "EmailField":
                    self.fields[field_name] = forms.EmailField(
                        required=field_required,
                        label=field_label,
                        widget=widget
                    )
                else:
                    print(f"WARNING - Tipo de campo desconocido: {field_type}")
        
        # Campo precioFinal
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
    # Agrega un asterisco rojo a los campos obligatorios
    def add_required_asterisk(self):
            for field_name, field in self.fields.items():
                if field.required:
                    field.label = mark_safe(f"<span class='asterisco'>*</span> {field.label}")