from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_alumnos(request):
    return HttpResponse('<h1>Alumnos</h1>')