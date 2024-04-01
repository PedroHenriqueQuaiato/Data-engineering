import math 
import cmath

def soma(a,b):
    return a + b

def divisão(a,b):
    return a / b


def subtração(a , b):
    return a - b 


def multiplicação(a,b):
    return a * b 

def Area_Circulo(Raio):
    return 3.14 * Raio**2


def pitagoras(a,b):
    c = a**2 + b**2
    resultado = math.sqrt(c)
    print('resultado:' , resultado)


def Area_circulo(Raio):
    Area = 3.14 * Raio**2
    print('resultado: ', Area)

def circunferencia(Raio):
    c = 2 * 3.14 * Raio
    print('resposta: ', c)

def analise(numeroPA):
    razão = numeroPA[1] - numeroPA[0] 
    print('A razão é: ', razão)


def Volume_cubo(ComprimentoCubo, alturaCubo, larguraCubo): 
    return ComprimentoCubo * alturaCubo * larguraCubo 
    

def é_Possivel(Base, Lado1, Lado2):
    if Base + Lado1 > Lado2 and Base + Lado2 > Lado1 and Lado1 + Lado2 > Base:
        return True
    else:
        return False


def Area_triangulo(Base, Lado1, Lado2):

    if é_Possivel(Base, Lado1, Lado2):
        print("É possível formar um triângulo.")
    else:
        print("Não é possível formar um triângulo.")


    if Base == Lado1 == Lado2:
        print('Tipo de triângulo: Equilátero')
    elif Base == Lado1 or Lado1 == Lado2 or Lado2 == Base:
        print('Tipo de triângulo: Isósceles')
    else:
        print('Tipo de triângulo: Escaleno')


#formula de Herão
    s = (Base + Lado1 + Lado2) / 2

    area = (s * (s - Base) * (s - Lado1) * (s - Lado2)) ** 0.5
    print("A área do triângulo é:", area)

    Perimetro = (Base + Lado1 + Lado2)
    print('Perimetro:', Perimetro)

# ANGULOS 

def angulos(Base, Lado1, Lado2):
    angulo_A = math.acos((Lado1**2 + Lado2**2 - Base**2)/ (2*Lado1*Lado2))
    angulo_B = math.acos((Lado2**2 + Base**2 - Lado1**2) / (2*Lado1*Base)) 
    angulo_C = math.acos((Base**2 + Lado1**2 - Lado2**2) / (2* Base*Lado1))

    angulo_A_graus = math.degrees(angulo_A)
    angulo_B_graus = math.degrees(angulo_B)
    angulo_C_graus = math.degrees(angulo_C)

    L1 = angulo_A_graus, angulo_B_graus,angulo_C_graus

    #resultados = angulos(Base, Lado1, Lado2)
    #print(f"Ângulo A: {resultados[0]:.2f} graus")
    #print(f"Ângulo B: {resultados[1]:.2f} graus")
    #print(f"Ângulo C: {resultados[2]:.2f} graus")


def Raiz_Quadrada():
    numeroRaiz = int(input("De que número quer descobrir a raiz:"))
    return math.sqrt(numeroRaiz)

def Area_retangulo(comprimento, largura): 
    return comprimento * largura
    

def baskara():
    A = float(input('Qual será o valor de A:'))
    B = float(input('Qual será o valor de B:'))
    C = float(input('Qual será o valor de C:'))

    Delta = (B**2) - 4 * A * C 
    print('valor de Delta:', Delta)

    Raiz_delta = math.sqrt(Delta)

    if Delta > 0:
        print('A equação terá dois valores reais e distintos')
    elif Delta == 0:
        print('A equação terá somente um valor real ou dois resultados iguais')
    else:
        print('A equação não possuirá valores reais ,somaou seja, são imaginarios')

    x1 = -B + Raiz_delta / 2*A
    print('Resultado de X1: ', x1)

    x2 = -B - Raiz_delta / 2*A
    print('resultado de X2: ', x2)


operação = input('Qual será a operação:')

if (operação == "soma"):
    a = int(input('Qual será o primeiro valor:'))
    b = int(input('Qual será o segundo valor: '))
    resultado = soma(a,b)
    print('resultado: ', resultado)

elif (operação == "subtração"):
    a = int(input('Qual será o primeiro valor:'))
    b = int(input('Qual será o segundo valor: '))
    resultado = subtração(a,b)
    print('resultado: ', resultado)

elif (operação == "multiplicação"):
    a = int(input('Qual será o primeiro valor:'))
    b = int(input('Qual será o segundo valor: '))
    resultado = multiplicação(a,b)
    print('resultado: ', resultado)

elif (operação == "divisão"):
    a = int(input('Qual será o primeiro valor:'))
    b = int(input('Qual será o segundo valor: '))
    resultado = divisão(a,b)
    print('resultado: ', resultado)

elif (operação == "Raiz"):
    resultado = Raiz_Quadrada()
    print ('Resultado: ', resultado)

elif (operação == "baskara"):
    resultado = baskara()        #assim que podemos chamar a função, pois lá em cima a função ja está com a formula, ou seja, a função tem seu manual de instruções, para saber o que fazer 

elif (operação == "Area Retangulo"):
    comprimento = int(input('Qual o valor do comprimento: '))
    largura = int(input('Qual o valor da largura:'))
    resultado = Area_retangulo(comprimento, largura)
    print('Área do retângulo:', resultado)

elif (operação == "Area Triangulo"):
    Base = int(input("Digite o valor da base: "))
    Lado1 = int(input("Digite o valor do lado 1: "))
    Lado2 = int(input("Digite o valor do lado 2: "))
    resultado = Area_triangulo(Base, Lado1, Lado2)

elif (operação == 'Area do circulo'):
    Raio = int(input("Qual o raio do circulo: "))
    resultado = Area_Circulo(Raio)
    print("Area do circulo: ", resultado)

elif (operação == "Volume do Cubo"):
    ComprimentoCubo = int(input('Qual o comprimento do cubo: '))
    larguraCubo =  int(input('Qual o largura do cubo: '))
    alturaCubo =  int(input('Qual o altura do cubo: '))
    resultado = Volume_cubo(ComprimentoCubo, alturaCubo, larguraCubo)
    print('Volume do cubo: ', resultado)

elif (operação == 'pitagoras'):
    a = int(input('valor A: '))
    b = int(input ('Valor B: '))
    resultado = pitagoras(a,b)
    
elif (operação == "circunferencia"):
    Raio = int(input('qual é o Raio: '))
    resultado = circunferencia(Raio)

elif (operação == "Area do circulo"): 
    Raio = int(input('Qual é o Raio: '))
    resultado = Area_Circulo(Raio)

else:
    numeroPA = [] 
    QuantidadeNumericadaPA = int(input('quantidade de numeros da P.A: '))  
    for i in range(QuantidadeNumericadaPA):      
      numeros = int(input('coloque os numeros: '))  
      numeroPA.append(numeros)
    
analise(numeroPA)

     








    




     


    
    


    

   