lista = []
Quantidade = int(input('Qual a quantidade de numeros na lista: '))
for i in range(Quantidade):
    numeros = int(input('Insira um numero: '))
    lista.append(numeros)

print(lista)

def descoberta(lista):
    razao = lista[1] - lista[0]
    termo = int(input('Qual o termo desejado: '))
    num = lista[0] + (termo - 1) * razao
    print('Esse é o numero encontrado: ', num)
    print('Essa é a razão: ', razao)

descoberta(lista)
    