from django import forms

class AddProdutoForm(forms.Form):
    nome = forms.CharField(label='Nome do novo produto', max_length=300)
