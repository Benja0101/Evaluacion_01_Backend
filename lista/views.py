
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Contacto
from .forms import ContactoForm

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

def eliminar_contacto(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    contacto.delete()
    return redirect('lista_contactos')

def detalle_contacto(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    return render(request, 'lista/detalle.html', {'contacto': contacto})


def lista_contactos(request):
    query = request.GET.get('q')
    # Filtrar los contactos por nombre o correo usando Q para OR
    if query:
        contactos = Contacto.objects.filter(Q(nombre__icontains=query) | Q(correo__icontains=query))
    else:
        contactos = Contacto.objects.all()
    return render(request, 'lista/lista.html', {'contactos': contactos})




def agregar_contacto(request):
    if request.method == 'POST':
        form  = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_contactos')
    else:
        form = ContactoForm()
    return render(request, 'lista/agregar.html', {'form': form})
        
    

# Create your views here.
