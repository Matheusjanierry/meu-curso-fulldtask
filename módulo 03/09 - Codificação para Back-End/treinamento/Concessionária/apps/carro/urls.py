from django.urls import path
from.views import *


urlpatterns = [
    path("", linkInicial, name= 'pagina_index'),
    path("", linkCadastro, name= 'pagina_cadastro'),
    path ("", linkCliente, name= 'pagina_cliente'),
    path("", linkVendedor, name= 'pagina_vendedor'),
    path("", linkProduto, name= 'pagina_produto')
]
