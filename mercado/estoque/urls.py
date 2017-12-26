from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('produtos/', views.produtos, name="produtos"),
    path('compra/', views.compra, name="compra")
]
