from django.shortcuts import render
from estoque.models import Produto, Compra
from .forms import AddProdutoForm, CompraLevaProdutosForm
from django.db.models import Sum
import logging


def index(request):
    return render(request, 'estoque/home.html')

def produtos(request):
    if request.method == 'POST':
        # Recebeu nome de um novo produto pelo form
        form = AddProdutoForm(request.POST)
        if form.is_valid():
            nome_novo =  form.cleaned_data['nome']
            produto_novo = Produto(nome=nome_novo)
            produto_novo.save()

    form = AddProdutoForm()
    produto_list = Produto.objects.all().order_by("nome").annotate(estoque=Sum('compra__quantidade'))

    return render(request, 'estoque/produtos.html', {'produto_list': produto_list, 'form': form})

def compra(request):
    if request.method == 'POST':
        #recebeu requisição de compra
        form = CompraLevaProdutosForm(request.POST)
        if form.is_valid():
            produto = form.cleaned_data['produto']
            quantidade = form.cleaned_data['quantidade'] 
            # multiplicando por 100 pois armazenamos com BigInt e não com decimal (sem perder a representação dos centavos)
            valor = int(float(form.cleaned_data['valor'] * 100))
            compra = Compra(quantidade=quantidade, valor=valor, produto=produto, valor_medio=1)
            compra.save()


    form = CompraLevaProdutosForm()
    return render(request, 'estoque/compra.html', {'form': form})