
from django.contrib import admin
from django.urls import path

from . import views
from alumnos.views import index_alumnos
from asignaturas.views import index_asignatura
from maestros.views import index_maestros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('alumnos/', index_alumnos),
    path('asignaturas/', index_asignatura),
    path('maestros/', index_maestros)
]
