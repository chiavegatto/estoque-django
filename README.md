# Desafio WPensar BACK-END
Desenvolvido por Gustavo Pergola
Prazo: 29/12 11:59
**Trello:** https://trello.com/b/TOzbvggQ/estoque-wpensar

## Tecnologias utilizadas
* Python 3.5.2
* Django 2.0

## Obeservações sobre tomadas de decisão 

Foi escolhido o tipo BigInteger para suportar o dinheiro, manipulando com divisões ou multiplicações por 100.
Tal escolha permite a simplicidade do projeto além de garantir comprar com valores de alguns trilhões, cobrindo todos casos possíveis.

## Requisitos

Você tem que desenvolver um sistema de estoque para um supermercado.

Esse supermercado assume que sempre que ele compra uma nova leva de produtos, ele tem que calcular o preço médio de compra de cada produto para estipular um preço de venda.
Para fins de simplificação assuma que produtos que tenham nomes iguais, são o mesmo produto e que não existe nem retirada e nem venda de produtos no sistema.

O valor calculado de preço médio deve ser armazenado.

Seu sistema deve ter:

1. Cadastro de produtos (Nome) -- OK
2. Compra de produtos (Produto, quantidade e preço de compra)
3. Listagem dos produtos comprados separados por compra (Nome, quantidade, preço de compra, preço médio)
4. Ser fácil de configurar e rodar em ambiente Unix (Linux ou Mac OS X)
5. Ser WEB -- OK
6. Ser escrita em Python 3.4+ -- OK
7. Só deve utilizar biliotecas livres e gratuitas -- OK

Esse sistema não precisa ter, mas será um plus:

1. Autenticação e autorização (se for com OAuth, melhor ainda)
2. Ter um design bonito
3. Testes automatizados