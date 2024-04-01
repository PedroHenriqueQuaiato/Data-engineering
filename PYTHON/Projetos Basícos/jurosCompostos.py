def jurosCompostos(tempo, taxa, investimento):
    montante = investimento * (1 + taxa / 100) ** tempo
    return montante

tempo = int(input('Informe o tempo: '))
taxa = float(input('Informe a Taxa: '))
investimento = float(input('Informe o valor inicial: '))

resultado = jurosCompostos(tempo, taxa, investimento)
print('Esse será o valor com os juros: ', resultado)




        
               


