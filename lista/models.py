from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from django.core.exceptions import ValidationError

def validar_telefono_chileno(valor):
    """
    Valida que el número de teléfono tenga el formato: +569XXXXXXXX
    Donde X son dígitos y el largo total es 12 caracteres
    """
    if not valor.startswith('+569'):
        raise ValidationError(
            'El número debe comenzar con +569 (formato chileno)'
        )
    if len(valor) != 12:
        raise ValidationError(
            'El número debe tener exactamente 12 caracteres (+569 + 8 dígitos)'
        )
    if not valor[4:].isdigit():
        raise ValidationError(
            'Los últimos 8 caracteres deben ser números'
        )

def validar_correo_largo(valor):
    """
    Valida que el correo electrónico no exceda los 150 caracteres
    """
    if len(valor) > 150:
        raise ValidationError(
            'El correo electrónico no puede exceder los 150 caracteres'
        )

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(
        max_length=12,  # Exactamente +569XXXXXXXX (12 caracteres)
        validators=[
            RegexValidator(
                r'^\+569\d{8}$',
                message='Ingrese un teléfono válido en formato +569XXXXXXXX (ej: +56912345678)'
            ),
            validar_telefono_chileno
        ],
        help_text='Formato: +569XXXXXXXX (número chileno)'
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
    