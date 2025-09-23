from django.db import models
from django.core.validators import RegexValidator,EmailValidator
# Create your models here.


class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(
        max_length=9,
        validators=[RegexValidator(r'^\d{9}$', message='Ingrese un teléfono válido de 9 dígitos, sin espacios ni símbolos.')]
    )
    correo = models.EmailField(unique=True, validators=[EmailValidator()])
    direccion = models.CharField(max_length=255)
    