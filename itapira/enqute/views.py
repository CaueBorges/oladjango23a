from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Olha, se voce não me ama.<h1><h2>Caneta azul, azul caneta<h2>")

# Create your views here.
