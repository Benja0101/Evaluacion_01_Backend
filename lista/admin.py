from django.contrib import admin
from .models import Contacto


@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    """Admin optimizado para Contactos con búsqueda por nombre/email y exportación CSV."""
    
    # Campos mostrados en la lista
    list_display = ("nombre", "correo", "telefono")
    
    # Búsqueda optimizada por nombre y email
    search_fields = ["nombre", "correo"]
    
    # Ordenar por nombre por defecto lo que hace es ordenar por defecgo los nombres
    ordering = ["nombre"]
    
    # 25 items por página (balance entre rendimiento y usabilidad)
    list_per_page = 25

    def exportar_csv(self, request, queryset):
        """Exporta los contactos seleccionados a CSV."""
        import csv
        from django.http import HttpResponse
        
        # Configurar respuesta CSV
        response = HttpResponse(content_type="text/csv; charset=utf-8")
        response["Content-Disposition"] = 'attachment; filename="contactos.csv"'
        response.write('\ufeff')  # BOM para Excel
        
        # Escribir CSV
        writer = csv.writer(response)
        writer.writerow(["Nombre", "Email", "Teléfono"])  # Headers en español
        
        for obj in queryset:
            writer.writerow([obj.nombre, obj.correo, obj.telefono])
        return response
    
    
    
    #exportar el usuario a csv
    exportar_csv.short_description = "Exportar a CSV"
    
    actions = ["exportar_csv"]  # Solo la acción de exportar



