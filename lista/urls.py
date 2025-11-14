from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView
)

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"contactos", views.ContactoViewSet)

urlpatterns = [

    # Rutas API REST
    path("api/", include(router.urls)),  # <- Aquí va el router

    # Autenticación API Rest Framework (Login básico)
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),

    # JWT
    # Aceptar con y sin slash final para evitar errores al POSTear desde clientes
    path("api/token", TokenObtainPairView.as_view(), name="token_obtain_pair_no_slash"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh", TokenRefreshView.as_view(), name="token_refresh_no_slash"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # Rutas HTML de la app contactos
    path("", views.lista_contactos, name="lista_contactos"),
    path("agregar/", views.agregar_contacto, name="agregar_contacto"),
    path("detalle/<int:pk>/", views.detalle_contacto, name="detalle_contacto"),
    path("editar/<int:pk>/", views.editar_contacto, name="editar_contacto"),
    path("eliminar/<int:pk>/", views.eliminar_contacto, name="eliminar_contacto"),
]
