
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from .models import Contacto
from .forms import ContactoForm
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from .serializers import GroupSerializer, UserSerializer, ContactoSerializer




class ContactoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contactos to be viewed or edited.
    """

    queryset = Contacto.objects.all().order_by("nombre")
    serializer_class = ContactoSerializer
    #permission_classes = [permissions.IsAuthenticated]
#api endpoint para usuarios

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]
# api endpoint para grupos


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    #permission_classes = [permissions.IsAuthenticated]





#Function-based views para la aplicación de contactos
def editar_contacto(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    if request.method == 'POST':
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contacto actualizado correctamente.')
            return redirect('lista_contactos')
    else:
        form = ContactoForm(instance=contacto)
    return render(request, 'lista/formulario.html', {'form': form, 'contacto': contacto})
#se edita el contacto existente utilizando un formulario prellenado con los datos actuales del contacto. luego de guardar los cambios, se redirige a la lista de contactos con un mensaje de éxito.
# View para eliminar un contacto
def eliminar_contacto(request, pk):
    # Obtener el contacto a eliminar
    contacto = get_object_or_404(Contacto, pk=pk)
    contacto.delete()
    messages.success(request, 'Contacto eliminado correctamente.')
    return redirect('lista_contactos')

# View para ver el detalle de un contacto
def detalle_contacto(request, pk):
    # Obtener el contacto por su clave primaria (pk)
    contacto = get_object_or_404(Contacto, pk=pk)
    return render(request, 'lista/detalle.html', {'contacto': contacto})

# View para listar contactos con funcionalidad de búsqueda
def lista_contactos(request):
    query = request.GET.get('q')
    # Filtrar los contactos por nombre o correo usando Q para OR
    if query:
        contactos = Contacto.objects.filter(Q(nombre__icontains=query) | Q(correo__icontains=query))
    else:
        contactos = Contacto.objects.all()
    return render(request, 'lista/lista.html', {'contactos': contactos})



# View para agregar un nuevo contacto
def agregar_contacto(request):
    if request.method == 'POST':
        form  = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            # Mensaje con tag específico para creación (se mostrará destacado)
            messages.success(request, 'Contacto creado correctamente.', extra_tags='created')
            return redirect('lista_contactos')
    else:
        form = ContactoForm()
        # Renderizar el formulario vacío
    return render(request, 'lista/agregar.html', {'form': form})
        
    



