from django.urls import path
from . import views
from django.urls import include, path
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
# URL patterns para la aplicación de contactos
urlpatterns = [
    
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),

    path('', views.lista_contactos, name='lista_contactos'),
    path('agregar/', views.agregar_contacto, name='agregar_contacto'),

    # URL para el detalle de contacto
    path('detalle/<int:pk>/', views.detalle_contacto, name='detalle_contacto'),
    # URL para editar contacto
    path('editar/<int:pk>/', views.editar_contacto, name='editar_contacto'),
    # URL para eliminar contacto
    path('eliminar/<int:pk>/', views.eliminar_contacto, name='eliminar_contacto'),
    path('api-auth/', include(router.urls)),

]
#este archivo contiene las URLs de la aplicación de contactos