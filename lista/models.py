from django.db import models
from django.core.validators import RegexValidator,EmailValidator
# Create your models here.


class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(
            max_length=15,
            validators=[RegexValidator(r'^\+?\d{9,15}$', message='Ingrese un teléfono válido con prefijo internacional, por ejemplo: +56912345678')]
        )
    correo = models.EmailField(unique=True, validators=[EmailValidator()])
    direccion = models.CharField(max_length=255)
    