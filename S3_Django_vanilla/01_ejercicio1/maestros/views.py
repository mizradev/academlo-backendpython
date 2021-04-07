from django.shortcuts import render
from django.http import HttpResponse

def index_maestros(request):
    return HttpResponse('<h1>Maestros</h1>')
