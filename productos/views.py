from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
from .models import producto


def index(request):
    productos = producto.objects.order_by('p_neto')
    return render_to_response('index.html', {'productos': productos})

"""
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

    """