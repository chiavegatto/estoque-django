from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *


@login_required(login_url='/login/')
def index(request):
    return render(request, 'estoque/home.html')

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def compra(request):
    form = CompraLevaProdutosForm()

    if request.method == 'POST':
        #recebeu requisição de compra
        form = CompraLevaProdutosForm(request.POST)
       
        if form.is_valid():
            compra = form.save()
            messages.add_message(request, messages.SUCCESS, 'Compra de ' + compra.__str__() + 's efetuada com sucesso.')
        else:
            return redirect('compra')
        form = CompraLevaProdutosForm() # reseta o form para aparecer em branco quando retornar
        
    
    heading = "Comprando Produtos"

    return render(request, 'estoque/compra.html', {'form': form})

@login_required(login_url='/login/')
def compra_edit(request, id):
    compra = get_object_or_404(Compra, id=id)
    form = CompraLevaProdutosForm(request.POST or None, instance=compra)
    
    if request.method == 'POST':
        # recebeu pedido de editar a compra
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Compra editada com sucesso.')
        else:
            return redirect('/compra/' + str(id))

    return render(request, 'estoque/compra_edit.html', {'form': form, 'compra': compra})

@login_required(login_url='/login/')
def listagem_compras(request):
    compra_list = Compra.objects.all()
    return render(request, 'estoque/listagem_compras.html', {'compra_list': compra_list})

@login_required(login_url='/login/')
def deletar_compra(request, id):
    compra = get_object_or_404(Compra, id=id)
    descricao_compra = compra.__str__()
    compra.delete()
    messages.add_message(request, messages.SUCCESS, 'Compra de ' + descricao_compra + 's deletada com sucesso.')
    return redirect('listagem_compras')


@login_required(login_url='/login/')
def logout(request):
    messages.add_message(request, messages.SUCCESS, 'Logout efetuado com sucesso.')
    auth_logout(request)
    return redirect('login')

def login(request):
    # Checa se o usuário já está logado
    if request.user.is_authenticated:
        messages.add_message(request, messages.WARNING, 'Você já está logado.')
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.add_message(request, messages.SUCCESS, 'Login efetuado com sucesso.')
                return redirect('home')
        
        messages.add_message(request, messages.ERROR, 'Combinação usuário/senha incorreta.')


    form = LoginForm(None)
    return render(request, 'estoque/login.html', {'form': form})


def registrar(request):
    
    # Checa se o usuário já está logado
    if request.user.is_authenticated:
        messages.add_message(request, messages.WARNING, 'Você já está logado.')
        return redirect('home')
    
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user_password = form.cleaned_data['password']
            user.set_password(user_password)
            user.save()
            messages.add_message(request, messages.SUCCESS, 'Cadastro efetuado com sucesso.')
            return redirect('login')

        messages.add_message(request, messages.ERROR, 'Opa, algo aconteceu. Talvez você esteja escolhendo um usuário já existente?')
    
    form = UsuarioForm(None)
    return render(request, 'estoque/registrar.html', {"form": form})

    
