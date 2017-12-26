from django.shortcuts import render
from estoque.models import Produto
from .forms import AddProdutoForm

def index(request):
    return render(request, 'estoque/home.html')

def produtos(request):
    if request.method == 'POST':
        # Recebeu nome de um novo produto pelo form
        form = AddProdutoForm(request.POST)
        if form.is_valid():
            # TODO Adiciona novo produto no bd
            nome_novo =  form.cleaned_data['nome']
            produto_novo = Produto(nome=nome_novo)
            produto_novo.save()

    form = AddProdutoForm()
    produto_list = Produto.objects.all().order_by("nome")
    
    
    return render(request, 'estoque/produtos.html', {'produto_list': produto_list, 'form': form})

def compra(request):
    return render(request, 'estoque/compra.html')