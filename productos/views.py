from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
from .models import Producto


def index(request):
    productos = Producto.objects.order_by('p_neto')
    return render_to_response('productos.html', {'productos': productos})


def detalle(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'detalle.html', {'producto': producto})
"""
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

"""