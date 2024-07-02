from django.shortcuts import render


def linkInicial(request):
    return render(request, 'index.html')
def linkProduto(request):
    lista_produto = produto.objects.all()
    return render(request, 'produto.html', {'produto': lista_produto})