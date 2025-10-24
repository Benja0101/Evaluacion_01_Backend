# lista/forms.py
from django import forms
from .models import Contacto
# Formulario para el modelo Contacto con estilos CSS personalizados
class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'telefono', 'correo', 'direccion']
# Agregar clases CSS a los widgets para mejorar la apariencia
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'border p-2 rounded w-full'})
    