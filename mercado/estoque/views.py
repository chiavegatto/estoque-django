from django.shortcuts import render, get_object_or_404
from estoque.models import Produto

def index(request):
    return render(request, 'estoque/home.html')

def produtos(request):
    produto_list = Produto.objects.all().order_by("nome")
    return render(request, 'estoque/produtos.html', {'produto_list': produto_list})

def produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    return render(request, 'estoque/produto_single.html', {'produto': produto})
