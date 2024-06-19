from django.urls import path
from .views import *

urlpatterns = [
    path("", pagina_inicial, name="pg_inicial"),
    path("pacientes", paginapacientes, name="pg_pacientes"),
    path("doutores", paginadoutores, name="pg_doutores")
]
