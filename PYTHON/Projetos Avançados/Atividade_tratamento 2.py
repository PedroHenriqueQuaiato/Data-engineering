import pandas as pd 
import matplotlib.pyplot as plt 

arquivo = pd.read_csv(r"C:\Users\pedro\Downloads\Evolution_DataSets.csv")

time = arquivo['Time']  # Declarei uma variavel para o coluna Time do dataFrame 
cranio = arquivo['Cranial_Capacity'] # Declarei uma variavel para o coluna Cranial_Capacity do dataFrame 

count_africa = arquivo['Location'].str.count('Africa').sum()   # Aqui usei essa codigo para contar as strings da coluna location, no caso contar quantas fezes aparece africa, e com isso fazer um grafico 
count_asia = arquivo['Location'].str.count('Asia').sum()
count_europa = arquivo['Location'].str.count('Europa').sum()  #or fim, somamos todas as contagens encontradas anteriormente, ou seja, somamos o número de vezes que 'Europa' aparece em todas as entradas da coluna 'Location'.


def soma (time,cranio,arquivo):          # Essa função adciona uma nova coluna chamada Time & Cranio
    result = time * cranio
    arquivo['Time & Cranio'] = result   # Aqui eu crio uma nova coluna no data frame (coloco o: Nome do arquivo['Nome da coluna'] = resultado para adiocionar ou dado que deseja adicionar)

def coluna (arquivo,time):
    resultado = time * 2
    arquivo ['TESTE'] = resultado

coluna (arquivo,time)
soma(time,cranio,arquivo)   

locations = ['Africa', 'Asia', 'Europa']
counts = [count_africa, count_asia, count_europa]

plt.bar(locations, counts)
plt.xlabel('Localização')                           # Essa parte serve para criar o grafico de barras conforme os dados do DaraFrame 
plt.ylabel('Contagem')
plt.title('Contagem de Localizações')
plt.show()


