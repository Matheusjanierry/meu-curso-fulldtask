from django.urls import path
from.views import *


urlpatterns = [
    path('', Listageral, name= "pg_inicial")
]
