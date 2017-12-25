from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=300)


    def __str__(self):
        return self.nome

