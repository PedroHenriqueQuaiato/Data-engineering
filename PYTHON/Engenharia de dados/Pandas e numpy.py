import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Constantes matematicas em NUMPY
print(np.e)
print(np.pi)
 
    # Funcções de trigonometria

angulo = np.pi/4
print(np.cos(angulo))  # np = nome da biblioteca a cima COS = cosseno da conta representado com Cos 
print(np.tan(angulo))
print(np.sin(angulo))


#Trabalhando com listas em python usando numpy

x = [1,2,3,4,5,6]
print(x)

#concatenação de arrys 

x = [1,2,3,4,5]
y = [6,7,8,9,10]

print(x + y)
print(np.sum(x)) # Soma atravez da funções sum todo o arry X (Soma tudo dentro de um ARRY)
print(np.add(x,y)) # Soma os numeros dos dois arrys (como se fossem matrizez, Exemplo: o 6 do arry Y + 1 do arry x = 7 na posição do arry resultante)
print(np.dot(x,y)) #

#para retornar uma posição especifica 

print(x[1]) #colocar dentro   do []

#percorrer listas

x = [10, 20, 30, 40, 50, 60, 70, 80, 90]

for i in x:
    print("Sin({0}) = {1:8.5f}"
          .format(i, np.sin(i))) # cacucula o seno de todos os numeros do arry 

#print("Sin({0}) = {1:8.5f}" Essa parte se refere au formato em que vou passar, ou seja, onde vai entrar cada coisa 
#.format(i, np.sin(i))) Esse já mostra o que vai entrar em cada espaço do codigo a cima.
    
#--------------------------------------------------------------------

#DICIONARIOS 
    
quimica = {'CH4': 16.04, 'H2O': 18.02, 'O2':32.00, 'CO2': 44.01}
quimica

#Assim que podemos adicionar um elemento para nosso dicionario

quimica['C8H18'] = 114.23
quimica

#Assim que podemos consultyar algo especifico em nosso dicionario 

quimica['CH4']

#Assim que podemos trazer resposta com o FOR

for composto, massa in quimica.items():
    print(f"A massa molar de {composto} é {massa:.2f}")

