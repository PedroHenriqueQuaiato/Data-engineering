import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1) # linspace para criar numeroa leatorios entre o e 10
y = np.sin(x)
z = np.cos(x)

print(x)

# Fazer um gráfico com isso
plt.plot(x, y, 'b', label='Seno') #O b Representa a cor do graico para um dos dados, no caso b de BLUE 
plt.plot(x, z, 'r', label='Coseno') # Label serve para colcoar os titulos 
plt.xlabel('Radianos') # para mostrar o titulo que vai ter o eixo x
plt.ylabel('Valor')# para mostrar o titulo que vai ter o eixo y
plt.title('Gráfico Demonstração') # Titulo do grafico 
plt.legend()
plt.grid(True) # mostra agrid atraz do grafico 
plt.show() # para mostrar 

# GRAFICOS MAIS AVANÇADOS 

plt.plot(y,z)
plt.axis('equal') # grafico em circulo 

# GRAFICOS MAIS SEPARADOS 

plt.subplot(2,1,1) # subplot usado para fazer um subplotagem em um imagem ( msotrar mais grafico em uma  imagem só)
plt.plot(x,z)
plt.title('Seno de X')
plt.show()


plt.subplot(2,1,1) # Esses numeros são o tamanho usado para fazer a plotagem 
plt.plot(x,y)
plt.title('Seno de Y')
plt.show()

