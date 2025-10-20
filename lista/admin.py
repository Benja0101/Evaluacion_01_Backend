from django.contrib import admin
from .models import Contacto


# Personalización del encabezado del sitio admin (opcional global)
admin.site.site_header = "Área de administración - Contactos"
admin.site.site_title = "Admin Contactos"
admin.site.index_title = "Panel de administración"


@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    """Admin personalizado para Contacto.

    Muestra los campos principales, permite búsqueda por los campos más útiles,
    añade filtros laterales y organiza el formulario con fieldsets.
    """

    list_display = ("nombre", "telefono", "correo", "direccion")
    search_fields = ("nombre", "correo", "telefono")
    list_filter = ("direccion",)
    ordering = ("nombre",)
    list_per_page = 20

    # Agrupar campos en el formulario de edición/creación
    fieldsets = (
        (None, {
            'fields': ("nombre", "correo")
        }),
        ("Contacto", {
            'fields': ("telefono", "direccion"),
            'classes': ('collapse',),
        }),
    )

    # Campos read-only opcionales (descomenta si quieres evitar edición)
    # readonly_fields = ("correo",)

    # Ejemplo de acción simple: marcar correo como 'enviado' (placeholder)
    def marcar_dummy(self, request, queryset):
        updated = queryset.count()
        self.message_user(request, f"Procesados {updated} contactos (acción dummy).")

    marcar_dummy.short_description = "Ejecutar acción dummy sobre los contactos"

    def exportar_csv(self, request, queryset):
        """Exporta los contactos seleccionados a un archivo CSV descargable."""
        import csv
        from django.http import HttpResponse
        from datetime import datetime

        now = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"contactos_{now}.csv"
        response = HttpResponse(content_type="text/csv; charset=utf-8")
        response["Content-Disposition"] = f"attachment; filename=\"{filename}\""

        writer = csv.writer(response)
        # Cabecera
        writer.writerow(["nombre", "telefono", "correo", "direccion"])

        for obj in queryset:
            writer.writerow([obj.nombre, obj.telefono, obj.correo, obj.direccion])
        return response

    exportar_csv.short_description = "Exportar seleccionados a CSV"

    actions = ("exportar_csv", "marcar_dummy")



