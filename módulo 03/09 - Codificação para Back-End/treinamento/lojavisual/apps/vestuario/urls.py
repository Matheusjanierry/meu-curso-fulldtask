from django.urls import path
from.views import *


urlpatterns = [
    path("", verindex, name= 'pagina_index'),
  
]