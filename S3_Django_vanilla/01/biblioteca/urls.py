
from django.contrib import admin
from django.urls import path

from autores.views import vista_autores

urlpatterns = [
    path('admin/', admin.site.urls),
    path('autores/', vista_autores)
]
