from django.contrib import admin
from estoque.models import Produto, Compra

admin.site.register(Produto)
admin.site.register(Compra)