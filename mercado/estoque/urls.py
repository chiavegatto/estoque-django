from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('registrar/', views.registrar, name="registrar"),
    path('produtos/', views.produtos, name="produtos"),
    path('compra/', views.compra, name="compra"),
    path('compra/<int:id>', views.compra_edit, name="compra_edit"),
    path('listagem_compras/', views.listagem_compras, name="listagem_compras")
]
