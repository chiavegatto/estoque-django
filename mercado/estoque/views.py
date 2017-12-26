from django.shortcuts import render
from estoque.models import Produto
from .forms import AddProdutoForm
from django.db.models import Sum

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
    return render(request, 'estoque/compra.html')