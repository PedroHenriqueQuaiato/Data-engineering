import matplotlib.pyplot as plt
import numpy as np 

cancelamentos = [
    {'cliente': 'João Silva', 'produto': 'Celular', 'valor_perdido': 1000},
    {'cliente': 'Maria Santos', 'produto': 'TV', 'valor_perdido': 2567},
    {'cliente': 'Pedro Oliveira', 'produto': 'Notebook', 'valor_perdido': 248},
    {'cliente': 'Ana Souza', 'produto': 'Fone de ouvido', 'valor_perdido': 354}
]

produto1 = []
valores1 = []


for i in cancelamentos:
   global produto
   produto = i['produto']
   produto1.append(produto)
   
for f in cancelamentos:
    global valores 
    valores = f['valor_perdido']
    valores1.append(valores)


plt.bar(produto1, valores1)

plt.title('Grafico de Cancelamentos')
plt.xlabel(produto1)
plt.ylabel(valores1)

plt.show()