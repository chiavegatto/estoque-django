from django.contrib import admin
from estoque.models import Produto, Compra

admin.site.register(Produto)

# @admin.register(Compra)
# class CompraAdmin(admin.ModelAdmin):
#   exclude = ('valor_medio',)
#   list_display = ('produto','quantidade','valor', 'valor_medio')
#   list_filter = ('produto','valor', 'quantidade', 'valor_medio')

admin.site.register(Compra)