from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response


def index(request):
    return render_to_response('index.html')