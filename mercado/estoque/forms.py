from django import forms
from .models import Produto, Compra
from django.contrib.auth.models import User

class AddProdutoForm(forms.ModelForm):
    nome = forms.CharField(label='', max_length=300, widget=forms.TextInput(attrs={'placeholder': 'Nome do Produto'}))

    class Meta:
        model = Produto
        fields = ('nome',)

class CompraLevaProdutosForm(forms.ModelForm):
    produto = forms.ModelChoiceField(queryset=Produto.objects.all(), empty_label="Selecione um produto", label='Produto')
    quantidade = forms.IntegerField(min_value=1, label='Quantidade', widget=forms.NumberInput(attrs={'placeholder': 'Quantidade'}))
    valor = forms.DecimalField(decimal_places=2, min_value=0.01, label='Valor em R$', widget=forms.NumberInput(attrs={'placeholder': 'Valor em R$'}))

    class Meta:
        model = Compra
        fields = ('produto', 'quantidade', 'valor',)
    
class UsuarioForm(forms.ModelForm):
    username = forms.CharField(label="",max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Usuário'}))
    email = forms.EmailField(label="",max_length=200, widget=forms.TextInput(attrs={'placeholder': 'E-mail'}))    
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class LoginForm(forms.Form):
    username = forms.CharField(label="", max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Usuário'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))