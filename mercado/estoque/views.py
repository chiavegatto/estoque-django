from django.shortcuts import render, get_object_or_404
from django.db.models import Sum
from django.contrib import messages

from .models import Produto, Compra
from .forms import AddProdutoForm, CompraLevaProdutosForm



def index(request):
    return render(request, 'estoque/home.html')


def produtos(request):
    if request.method == 'POST':
        # Recebeu nome de um novo produto pelo form
        form = AddProdutoForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Produto cadastrado com sucesso.')

    form = AddProdutoForm()
    produto_list = Produto.objects.all().order_by("nome").annotate(estoque=Sum('compra__quantidade'))

    return render(request, 'estoque/produtos.html', {'produto_list': produto_list, 'form': form})


def compra(request):
    form = CompraLevaProdutosForm()

    if request.method == 'POST':
        #recebeu requisição de compra
        form = CompraLevaProdutosForm(request.POST)
       
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Compra efetuada com sucesso.')
        
        form = CompraLevaProdutosForm() # reseta o form para aparecer em branco quando retornar
        
    
    heading = "Comprando Produtos"

    return render(request, 'estoque/compra.html', {'form': form})


def compra_edit(request, id):

    compra = get_object_or_404(Compra, id=id)
    form = CompraLevaProdutosForm(request.POST or None, instance=compra)
    
    if request.method == 'POST':
        # recebeu pedido de editar a compra
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Compra editada com sucesso.')

    return render(request, 'estoque/compra_edit.html', {'form': form, 'compra': compra})

def listagem_compras(request):

    compra_list = Compra.objects.all()
    return render(request, 'estoque/listagem_compras.html', {'compra_list': compra_list})