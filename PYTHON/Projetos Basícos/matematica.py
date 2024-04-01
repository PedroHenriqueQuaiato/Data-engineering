import math

def verifica_triangulo(Base, Lado1, Lado2):
    if (Lado1 + Lado2 > Base) and (Lado1 + Base > Lado2) and (Lado2 + Base > Lado1):
        return True
    else:
        return False

Base = int(input("Digite o valor da base: "))
Lado1 = int(input("Digite o valor do lado 1: "))
Lado2 = int(input("Digite o valor do lado 2: "))

if verifica_triangulo(Base, Lado1, Lado2):
    if Base == Lado1 == Lado2:
        print('Tipo de triângulo: Equilátero')
    elif Base == Lado1 or Lado1 == Lado2 or Lado2 == Base:
        print('Tipo de triângulo: Isósceles')
    else:
        print('Tipo de triângulo: Escaleno')

    s = (Base + Lado1 + Lado2) / 2
    area = (s * (s - Base) * (s - Lado1) * (s - Lado2)) ** 0.5
    print("A área do triângulo é:", area)

    Perimetro = (Base + Lado1 + Lado2)
    print('Perímetro:', Perimetro)

    try:
        resultados = angulos(Base, Lado1, Lado2)
        print(f"Ângulo A: {resultados[0]:.2f} graus")
        print(f"Ângulo B: {resultados[1]:.2f} graus")
        print(f"Ângulo C: {resultados[2]:.2f} graus")
    except ValueError as e:
        print(f"Erro ao calcular ângulos: {e}")
else:
    print("Os comprimentos dos lados não formam um triângulo válido.")
