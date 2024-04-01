import math

def é_Possivel(Base, Lado1, Lado2):
    if Base + Lado1 > Lado2 and Base + Lado2 > Lado1 and Lado1 + Lado2 > Base:
        return True
    else:
        return False


Base = int(input("Digite o valor da base: "))
Lado1 = int(input("Digite o valor do lado 1: "))
Lado2 = int(input("Digite o valor do lado 2: "))

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

    return angulo_A_graus, angulo_B_graus,angulo_C_graus

resultados = angulos(Base, Lado1, Lado2)
print(f"Ângulo A: {resultados[0]:.2f} graus")
print(f"Ângulo B: {resultados[1]:.2f} graus")
print(f"Ângulo C: {resultados[2]:.2f} graus")