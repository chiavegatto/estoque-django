# Desafio WPensar BACK-END
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](http://opensource.org/licenses/MIT)

Desenvolvido por Gustavo Pergola

Prazo: 29/12/2017 11:59 

**Trello do projeto:** https://trello.com/b/TOzbvggQ/estoque-wpensar

## Tecnologias utilizadas
* Python 3.5.2
* Django 2.0

## Como inicializar

#### Instalando as tecnologias necessárias
Instale python 3.5.2 ou superior

* Na maioria das distros Linux o python já vem pré instalado

* Para Mac OS X, use: `brew install python3`

            
Execute o comando para instalar o django:

        sudo pip3 install Django==2.0
Logo depois:

`git clone https://bitbucket.org/vipkry/querotrabalharnawpensar`

`cd querotrabalharnawpensar/mercado`

`python3 manage.py runserver`

  

Em seguida basta navegar para http://localhost:8000

* Se quiser fazer uso da página administrativa, crie um usuário adminstrativo com o comando:
        
        python3 manage.py createsuperuser

* Se quiser aplicar os testes automatizados:
        
        python3 manage.py test

## Requisitos

Você tem que desenvolver um sistema de estoque para um supermercado.

Esse supermercado assume que sempre que ele compra uma nova leva de produtos, ele tem que calcular o preço médio de compra de cada produto para estipular um preço de venda.
Para fins de simplificação assuma que produtos que tenham nomes iguais, são o mesmo produto e que não existe nem retirada e nem venda de produtos no sistema.

O valor calculado de preço médio deve ser armazenado.

Seu sistema deve ter:

1. Cadastro de produtos (Nome) -- OK
2. Compra de produtos (Produto, quantidade e preço de compra) -- OK
3. Listagem dos produtos comprados separados por compra (Nome, quantidade, preço de compra, preço médio) -- OK
4. Ser fácil de configurar e rodar em ambiente Unix (Linux ou Mac OS X) -- OK
5. Ser WEB -- OK
6. Ser escrita em Python 3.4+ -- OK
7. Só deve utilizar biliotecas livres e gratuitas -- OK

Esse sistema não precisa ter, mas será um plus:

1. Autenticação e autorização -- OK (Não foi utilizado OAuth)
2. Ter um design bonito -- OK
3. Testes automatizados -- OK