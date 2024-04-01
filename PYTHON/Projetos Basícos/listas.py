lista = [] 
quantidadeNumerica = int(input('Quantos números terão na lista: '))

for i in range(quantidadeNumerica):
    numeros =  int(input('Digite um número: '))
    lista.append(numeros)

def analise(lista):
    maiorNumero = max(lista) #maior numero 
    somaNumeros = sum(lista) # soma numeros do array 
    trazpraFrente = list(reversed(lista))
    
    print('lista norma: ', lista)
    print('Maior número na lista: ', maiorNumero)
    print('Soma de todos os números na lista: ', somaNumeros)
    print('Os numeros de traz para frente: ', trazpraFrente)
    

analise(lista)

