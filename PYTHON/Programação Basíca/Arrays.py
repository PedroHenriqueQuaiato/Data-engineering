
#   .remove 

numeros = [1,2,3,4,5,6,7]

print(numeros)

valor = int(input('qual numero deseja excluir:'))

numeros.remove(valor)

print(numeros)

# .append 

numeros = [1,2,3,4,5,6,7]

print(numeros)

valor = int(input('Valor que deseja adcionar:'))

numeros.append(valor)



# .pop

numero = [1,2,3,4,5,6,7]

print(numeros)

numero.pop(0) 
# aqui ele vai remover a 
#numero que estiver na posição 0, ou seja ou o 1


# ideia de pilha 

numeros = [1,2,3,4,5,6,7]

print(numeros)


valor = int(input('diga o valor '))
posição = int(input('defina uma posição'))

numeros.insert(posição, valor)

print(numeros)

# buscar numeros em um arry 

numero = [1,2,3,4,5,6,7,8,9,10]

numeros = int(input('informe um numero a ser buscado:')) # temos que colocar o 

print(numeros in numero ) #aqui tem que ser primeiro a variavel e depois deve ser o nome do arry 

