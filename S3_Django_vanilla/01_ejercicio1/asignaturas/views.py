from django.shortcuts import render
from django.http import HttpResponse


def index_asignatura(request):
    return HttpResponse('<h2>Asignaturas</h2>')
