import matplotlib as mtp

class Produto:
    def __init__(self,nome,preco,unidade_venda):
        self.nome = nome
        self.preco = preco 
        self.unidade_venda = unidade_venda         #Definir o que teremos na minha class
    
nome = input('Digite o nome do produto: ') 
preco = float(input('Digite o Valor do produto: '))
unidade_venda = input('digite qual a unidade de venda: ')   # tem que ficar fora da classe para ser acessado pelas funções 

produto = Produto(nome=nome, preco=preco, unidade_venda=unidade_venda)


def analise( preco,nome,unidade_venda,):
    if preco == None:
         print('Preço invlido, Preço deve ser maior que ZERO !')
    elif unidade_venda == None:
         print("Unidade Invalida, coloque alguam unidade")
    elif nome == None:
        print('Nome invalido, nome deve ser colocado !')
    else: 
        global lista     #Lista de esse global porque assim ele pode ser acesada por qualquer função de qualquer parte do codigo
        lista = [produto.nome, produto.preco, produto.unidade_venda]
        print(lista)

escolha = input('Deseja adicionar mais itens ? S/N: ')

def produtos (escolha):
    if escolha == 'S':
        global mais 
        mais = int(input('Qual o numero de produtos que deseja adcionar: '))
    else: 
        print('Até mais !')

    for i in range(mais):
        nome = input('Digite o nome do produto: ') 
        preco = float(input('Digite o Valor do produto: '))
        unidade_venda = input('digite qual a unidade de venda: ')

        lista.append(nome)
        lista.append(preco)
        lista.append(unidade_venda)
        print(lista)
        

analise(produto.nome, produto.preco, produto.unidade_venda)
produtos(escolha)

            




    


















