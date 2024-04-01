numeros = []
numero = int(input('digite os valores: ')) # é o inicial, para iniciar o codigo.
while (numero > 0):      #while é enquanto
    numeros.append(numero)
    numero = int(input('digite os valores: ')) # isso é a condição, ou seja, o que ele vai repetir 

print(numeros)

def numerospares(numeros):
    for numero in numeros:  #podemos ler o FOR como: "Para cada 'numero' na lista 'numeros'"
        if numero % 2 == 0:
            print('Esse numero é impar')
        else:
            print('Esse numero é Par')


numerospares(numeros)



    

