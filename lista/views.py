
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Contacto
from .forms import ContactoForm
# Create your views here.
def editar_contacto(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    if request.method == 'POST':
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect('lista_contactos')
    else:
        form = ContactoForm(instance=contacto)
    return render(request, 'lista/formulario.html', {'form': form, 'contacto': contacto})
# View para eliminar un contacto
def eliminar_contacto(request, pk):
    # Obtener el contacto a eliminar
    contacto = get_object_or_404(Contacto, pk=pk)
    contacto.delete()
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
            return redirect('lista_contactos')
    else:
        form = ContactoForm()
        # Renderizar el formulario vacío
    return render(request, 'lista/agregar.html', {'form': form})
        
    

# Create your views here.
