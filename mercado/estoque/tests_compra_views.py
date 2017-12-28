from django.test import TestCase
from .views import * 
from .models import *

class CompraViews(TestCase):

    # Classe representando os métodos:
        # compra
        # compra_edit
        # delete_compra
        # listagem_compra
 
    def setUp(self):
        # Seta um usuário para conseguir logar
        user = User(username='nome')
        user.set_password('pass')
        user.save()

        # Seta uma compra para evitar 404
        Produto.objects.create(nome="Produto1", valor_medio=0)
        Compra.objects.create(produto=Produto.objects.first(), valor=100, quantidade=100)

    def test_redireciona_anonimo_para_login_compra(self):
        # Testa o método COMPRA
        resposta = self.client.get('/compra', follow=True)
        self.assertRedirects(resposta, '/login/?next=/compra/', status_code=301)
        resposta = self.client.post('/compra', follow=True)
        self.assertRedirects(resposta, '/login/?next=/compra/', status_code=301)

    def test_redireciona_anonimo_para_login_compra_edit(self):
        # Testa o método COMPRA_EDIT
        resposta = self.client.get('/compra/1', follow=True)
        self.assertRedirects(resposta, '/login/?next=/compra/1')
        resposta = self.client.post('/compra/1', follow=True)
        self.assertRedirects(resposta, '/login/?next=/compra/1')

    def test_redireciona_anonimo_para_login_deletar_compra(self):
        # Testa o método DELETAR_COMPRA
        resposta = self.client.get('/deletar_compra/1', follow=True)
        self.assertRedirects(resposta, '/login/?next=/deletar_compra/1')
        resposta = self.client.post('/deletar_compra/1', follow=True)
        self.assertRedirects(resposta, '/login/?next=/deletar_compra/1')

    def test_redireciona_anonimo_para_login_listagem_compras(self):
        # Testa o método LISTAGEM_COMPRA
        resposta = self.client.get('/listagem_compras', follow=True)
        self.assertRedirects(resposta, '/login/?next=/listagem_compras/', status_code=301)
        resposta = self.client.post('/listagem_compras', follow=True)
        self.assertRedirects(resposta, '/login/?next=/listagem_compras/', status_code=301)


    def test_mostra_template_compra_view(self):
        # Testa a view COMPRA
        self.client.login(username='nome', password='pass')
        resposta = self.client.get('/compra/')
        self.assertEqual(resposta.status_code, 200)
        self.assertTemplateUsed(resposta, 'estoque/compra.html')

    def test_mostra_template_compra_edit_view(self):
        # Testa a view COMPRA_EDIT
        self.client.login(username='nome', password='pass')
        resposta = self.client.get('/compra/1')
        self.assertEqual(resposta.status_code, 200)
        self.assertTemplateUsed(resposta, 'estoque/compra_edit.html')
    
    def test_mostra_template_adeletar_compra_view(self):
        # Testa a view DELETAR_COMPRA
        self.client.login(username='nome', password='pass')
        resposta = self.client.get('/deletar_compra/1')
        # deletar compra não renderiza e sim redireciona
        self.assertRedirects(resposta, '/listagem_compras/') 
        
    def test_mostra_template_compra_edit_view(self):
        # Testa a view LISTAGEM_COMPRAS
        self.client.login(username='nome', password='pass')
        resposta = self.client.get('/listagem_compras/')
        self.assertEqual(resposta.status_code, 200)
        self.assertTemplateUsed(resposta, 'estoque/listagem_compras.html')

    def test_recusa_form_branco_compra_view(self):
        self.client.login(username='nome', password='pass')
        # pedido em branco
        resposta = self.client.post('/compra/', {}) 
        self.assertEqual(resposta.status_code, 302)

    def test_recusa_form_invalido_compra_view(self):
        # pedido invalido (parametro ruim)
        resposta = self.client.post('/compra/', {'quantidade': 100, 'valor': 100, 'produto': "produto teste"}) 
        self.assertEqual(resposta.status_code, 302)
        
    def test_aceita_form_valido_compra_view(self):
        self.client.login(username='nome', password='pass')
        # pedido certo
        produto = Produto.objects.first()
        resposta = self.client.post('/compra/', {'quantidade': 100, 'valor': 100, 'produto': produto.id}) 
        self.assertEqual(resposta.status_code, 200)

