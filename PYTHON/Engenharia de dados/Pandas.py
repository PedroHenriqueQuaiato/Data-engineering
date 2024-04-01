import pandas as pd 

#series são como arrys, porem possuem um INDEX

valores =pd.Series([1,2,3,4,5])
frutas = pd.Series(['banana', 'maça','uva '])
print(frutas)
print(frutas.values) # VALUES é para mostrar os valores so array
print(valores.values)

# Exemplo com series de numeros 

numeros = pd.Series([1,2,3,4,5,6,7,8,9,10])

print(numeros)  # mostra a lista do array de numeros 
print("========")
print(numeros.values) # values é o valor 
print('========')
print(numeros.index) #  estrutura de dados que rotula as linhas 
                    #ou entradas de um DataFrame ou Series. 
                    #O índice pode ser visto como uma espécie de 
                    #identificador único para cada linha de dados.


#Exemplos de series informando indices 

alunos = pd.Series([1,2,3,4], index = (["Pedro", "Alex", "Pablo"]))

print(alunos)
print(alunos.values)
print(alunos.index)
print(alunos['Pedro'])
print(alunos.index[0]) #Retona a posição 0 lá no index (devo colocar . pois é como se fosse um indicador do que eu quero dentro e alunos)

#----------------DATA FRAME -----------------------

data = {
    'banana': [1,2,4,6], # os Arrys devem ser do mesmo tamanho
    'maças': [9,7,4,2]

}

compras = pd.DataFrame(data)

print(compras)

compradores = pd.DataFrame(data, index = ['Pedro', 'Amanda', 'Ana', 'Marcelo'])
print(compradores)  # essas duas linhas de codigos, temos a seguinte mudança, enquanto no primeiro codigo 
# temos somente maças e bananas, no segundo demos a adição dos compradores, pois qunado adicionamos
# Eles, eles passam ser a linha horizontal, sendo assim (Pedro comprou 1 banana e 9 maças)
# O index pode ser entendido como a posição (ver com o carlos)

compras.loc['Ana']

