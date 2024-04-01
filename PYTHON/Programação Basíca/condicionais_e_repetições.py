def soma(a, b):
    return a + b

def divisao(a, b):
    return a / b

def calculadora(operacao, a, b):
    if(operacao == "soma"):       #nesse caso, a operação e especificada como "soma" (não importa se é espas duplas ou simples)                      # if = a se 
        resultado = (a, b)         # IF igual a "se"
        print(resultado)
    elif(operacao == "divisao"):   #elif é quando o primeiro não for verdadeiro, se tiver mais comparações pode colocar varios ELIF até chegar no else
        resultado = divisao(a, b)
        print(resultado)
    else:                           # esse e´quando os dois primeiros 
        print("Operação não existe!")
    
    
#------- cauculadora com parametros ---------------------------------------------------

def soma(a, b):
    return a + b

def divisao(a, b):          #são os parametros para passar 
    return a / b
    
def multiplicacao(a, b):
    return a * b

def calculadora():
    
    operacao = input("Informe a operação para ser realizada:")
    a = int(input("Informe o valor a:"))                          # aqui eu pedi os valores dentro da função, pois ali em baixo eu ja uso os parametros 
    b = int(input("Informe o valor b:"))                           # posso colocar esse comandos, no escopo global tambem 
    
    if(operacao == "soma"):
        resultado = soma(a, b)
        print(resultado)
    
    elif(operacao == "divisao"):
        resultado = divisao(a, b)
        print(resultado)
    
    elif(operacao == "multiplicacao"):
        resultado = multiplicacao(a, b)
        print(resultado)
   
    else:
        print("Erro, operação não existe!")
    
calculadora()

# -------------------SWITCH para python --------------------

def numerosEscrita(numero):
    match numero:              # match poderia ser entendi como correspondente, ou seja no caso estou falando se a função numero corresponder a alguns dos case a baixo ele retona uma mensagem
        case 0:                # case pode ser lido como caso ou caso que ( condilção)
            print('zero')
        case 1: 
            print('um')
        case 2: 
            print('dois')
        case 3:
            print('três')
        case default: 
            print('numero indefinido !')
        
numerosEscrita()