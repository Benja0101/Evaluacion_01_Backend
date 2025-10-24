from django.urls import path
from . import views
# URL patterns para la aplicación de contactos
urlpatterns = [
    path('', views.lista_contactos, name='lista_contactos'),
    path('agregar/', views.agregar_contacto, name='agregar_contacto'),

    # URL para el detalle de contacto
    path('detalle/<int:pk>/', views.detalle_contacto, name='detalle_contacto'),
    # URL para editar contacto
    path('editar/<int:pk>/', views.editar_contacto, name='editar_contacto'),
    # URL para eliminar contacto
    path('eliminar/<int:pk>/', views.eliminar_contacto, name='eliminar_contacto'),

]
#este archivo contiene las URLs de la aplicación de contactos