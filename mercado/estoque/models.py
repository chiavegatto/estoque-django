from django.db import models
from django.db.models import Sum
from django.core.validators import MinValueValidator

class Produto(models.Model):
    nome = models.CharField(max_length=300)
    valor_medio = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    def __str__(self):
        return self.nome

class Compra(models.Model):
    quantidade = models.IntegerField(validators=[MinValueValidator(1)])
    valor = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0.1)])
    
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.quantidade, self.produto.nome)

    #Override do método save() do modelo para calcular o valor_medio automaticamente
    def save(self, *args, **kwargs):
        quantidade_total = 0
        valor_total = 0

        super(Compra, self).save(*args, **kwargs)
        
        # pega compras relacionadas
        compras = Compra.objects.filter(produto=self.produto).aggregate(Sum('quantidade'), Sum('valor'))

        if compras['quantidade__sum'] is not None:
            # soma todas compras (qtd)
            quantidade_total += compras['quantidade__sum']
            # soma todas compras (valor)
            valor_total += compras['valor__sum']
        
        # calcula valor médio
        novo_valor_medio = valor_total / quantidade_total
        # atualiza produto relacionado
        produto = self.produto
        produto.valor_medio = novo_valor_medio
        produto.save()
        