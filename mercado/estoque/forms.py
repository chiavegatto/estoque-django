from django import forms
from .models import Produto, Compra
from django.contrib.auth.models import User

class AddProdutoForm(forms.ModelForm):
    nome = forms.CharField(label='Nome do novo produto', max_length=300)

    class Meta:
        model = Produto
        fields = ('nome',)

class CompraLevaProdutosForm(forms.ModelForm):
    produto = forms.ModelChoiceField(queryset=Produto.objects.all(), empty_label="Selecione um produto")
    quantidade = forms.IntegerField(min_value=1)
    valor = forms.DecimalField(decimal_places=2, min_value=0.01)

    class Meta:
        model = Compra
        fields = ('produto', 'quantidade', 'valor',)
    
class UsuarioForm(forms.ModelForm):
    username = forms.CharField(label="Seu nome de usuário", max_length= 300)
    password = forms.CharField(label="Sua senha", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password',)