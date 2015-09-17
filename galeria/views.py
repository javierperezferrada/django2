from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
from .models import Imagen


def galeria(request):
    imagenes = Imagen.objects.order_by('id')
    return render_to_response('galeria.html', {'imagenes': imagenes})


def d_imagen(request, imagen_id):
    imagen = get_object_or_404(Imagen, pk=imagen_id)
    return render(request, 'imagen.html', {'imagen': imagen})