import pandas as pd 
import numpy as np


arquivo = pd.read_csv(r"C:\Users\pedro\Downloads\archive\topyoutube.csv")

arquivo = arquivo.fillna('Não Informado')

arquivo ['Avg'] = arquivo['Avg'].round(2)
#Aqui usei o .Round para especificar duas casas após a virgula

quary = arquivo.query("Artist == 'Eminem'")

print(quary.head(5))

arquivo = arquivo.sort_values(by ='Total Views', ascending=False)
# nessa parte usamos o .SORT_Values para ordenar depois usamos o by para esopecificar a coluna 
#e depois usamos o ASCENDING = False para retornar do maior para o menos 
# Porem se colocarmos o True podemos obter no menor para o maior 
print(arquivo.head(10))

quar2 = arquivo.sort_values(by = 'Artist', ascending=True)

print(quar2.head(100))

arquivo = arquivo.to_csv("C:\\Users\\pedro\\OneDrive\\Área de Trabalho\\Curso engenharia de dados\\Projetos\\Tarefa.csv")






