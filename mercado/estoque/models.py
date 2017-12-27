from django.db import models
from django.core.validators import MinValueValidator

class Produto(models.Model):
    nome = models.CharField(max_length=300)

    def __str__(self):
        return self.nome

class Compra(models.Model):
    quantidade = models.IntegerField(validators=[MinValueValidator(1)])
    valor = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0.1)])
    valor_medio = models.DecimalField(max_digits=12, decimal_places=2)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.quantidade, self.produto.nome)

    #Override do método save() do modelo para calcular o valor_medio automaticamente
    def save(self, *args, **kwargs):
        self.valor_medio = self.valor / self.quantidade
        super(Compra, self).save(*args, **kwargs)