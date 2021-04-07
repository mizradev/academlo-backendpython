from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def vista_autores(request):
    return HttpResponse('<h1>Autores viesta</h1>')
