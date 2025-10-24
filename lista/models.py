from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from django.core.exceptions import ValidationError

def validar_telefono_chileno(valor):
    """
    Valida que el número de teléfono tenga el formato: +569XXXXXXXX
    Donde X son dígitos y el largo total es 12 caracteres.
    Solo permite '+' al inicio y números en el resto.
    """
    # Verificar que empiece con +569
    if not valor.startswith('+569'):
        raise ValidationError(
            'El número debe comenzar con +569 (formato chileno)'
        )
    
    # Verificar longitud exacta
    if len(valor) != 12:
        raise ValidationError(
            'El número debe tener exactamente 12 caracteres (+569 + 8 dígitos)'
        )
    
    # Verificar que después del + solo haya dígitos
    resto = valor[1:]  # todo después del +
    if not resto.isdigit():
        raise ValidationError(
            'Solo se permite el símbolo + al inicio, el resto deben ser números'
        )
        
    # Verificar que no haya espacios ni otros caracteres
    if any(c for c in valor if c not in '+0123456789'):
        raise ValidationError(
            'Solo se permiten números y el símbolo + al inicio'
        )

def validar_correo_largo(valor):
    """
    Valida que el correo electrónico no exceda los 150 caracteres
    """
    if len(valor) > 150:
        raise ValidationError(
            'El correo electrónico no puede exceder los 150 caracteres'
        )
# Modelo Contacto con validaciones personalizadas
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(
        max_length=12,  # Exactamente +569XXXXXXXX (12 caracteres)
        validators=[
            RegexValidator(
                r'^\+[0-9]+$',  # Permite + solo al inicio, seguido únicamente de números
                message='Solo se permite el símbolo + al inicio, seguido de números'
            ),
            validar_telefono_chileno
        ],
        help_text='Formato: +569XXXXXXXX (solo números después del +)',
        error_messages={
            'invalid': 'Ingrese solo el símbolo + al inicio seguido de números',
        }
    )
    correo = models.EmailField(
        unique=True,
        max_length=150,
        validators=[
            EmailValidator(message='Ingrese un correo electrónico válido'),
            validar_correo_largo
        ],
        help_text='Máximo 150 caracteres'
    )
    direccion = models.CharField(max_length=255)
    