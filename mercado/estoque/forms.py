from django import forms
from .models import Produto

class AddProdutoForm(forms.Form):
    nome = forms.CharField(label='Nome do novo produto', max_length=300)

class CompraLevaProdutosForm(forms.Form):
    produto = forms.ModelChoiceField(queryset=Produto.objects.all(), empty_label="Selecione um produto")
    quantidade = forms.IntegerField(min_value=1)
    valor = forms.DecimalField(decimal_places=2)
    
