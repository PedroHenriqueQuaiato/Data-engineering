import matplotlib.pyplot as plt
import numpy as np


labels = ['A', 'B', 'C', 'D']
valores = [10, 20, 15, 25]

# Criando o gráfico de barras
plt.bar(labels, valores)

# Adicionando títulos e rótulos aos eixos
plt.title('Gráfico de Barras')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Exibindo o gráfico
plt.show()