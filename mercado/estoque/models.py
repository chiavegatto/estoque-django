from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=300)

    def __str__(self):
        return self.nome

class Compra(models.Model):
    quantidade = models.IntegerField()
    valor = models.BigIntegerField()
    valor_medio = models.BigIntegerField()
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.quantidade, self.produto.nome)
