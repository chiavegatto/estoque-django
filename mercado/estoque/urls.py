from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('produtos/', views.produtos),
    path('produto/<id>/', views.produto, name='produto'),
]
