numero = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for numeros in numero:
    print(numeros)

    # for serve para percorrer ou olhar todo a arry 

for i in range(0, 4):
    print("i:", i)
    for j in range (0, 3):
        print("j:", j)

#----------------------------------------------------

valores = [10, "Emanoel", True, 10]
inteiros = []
textos = []
logicos = []

for valor in valores:
    if(type(valor) is int):
        inteiros.append(valor)
    if(type(valor) is str):
        textos.append(valor)
    if(type(valor) is bool):
        logicos.append(valor)
        
print(inteiros)
print(textos)
print(logicos)


 # ------------------------------------while------------------------------LOOPS

numeros = []
numero = int(input("Informe um número inteiro:"))
while (numero > 0):    #Ele é uma condição para para o codigo, no caso desse codigo ele vai analisar se o numero for maiorque 0 ele continua e não le para 
    numeros.append(numero)
    numero = int(input("Informe um número inteiro:"))

print(numeros)

#--------------------------------------FOR----------------------------------

numero = []    #crie o ARRAY
QuantidadeNumericadaPA = int(input('Quantidade de numeros da P.A.: '))   #Aqui estou pedindo quantos numero vai ser, pois podem ser muitos ou poucos numeros, e diferente tipos negativo, positivo, virgula
for i in range(QuantidadeNumericadaPA):   # aqui nesse parte basicamente estou dizendo quantos numeros que eu tenho na sequencia, a função range serve para contar, ou seja quantas vezes ele vai executar (o i é uma variavel, posso dar qualquer nome), PODEMOS LER ISSO DO SEGUINTE MODO: "Para cada 'i' no intervalo." range PODE SER LIDO COMO INTERVALO DE 5 POR EXEMPLO
        numeros = int(input('Digite número da P.A: '))   # o i serve como um contador, (ele é um variavel) em resumo o i representa os valores 
        numero.append(numeros)      # aqui serve para adicionar os numeros na variavel 'numero' que é o meu array

print('A sequência é:', numero)

def analise(numero):
  razão = numero[1] - numero[0] # aqui tem a variavel que é um array, eu chamo as pocições dessa forma [0] - aqui usei a pocição 1
  print('A razão é: ', razão)

analise(numero)


#range e quantas vezes vou executar a linha de codigo


