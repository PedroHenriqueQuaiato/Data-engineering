salariodoVendedor = 1500.00
vendas = float(input('Valor de vendas no mês: '))

if vendas == 1000 or vendas < 5000:
    salario = salariodoVendedor + 500.00
    print('Esse é o valor total do salario com o bonus: ',salario)

elif vendas == 5000 or vendas <= 7500.00:
    salario = salariodoVendedor + 700.00
    print("Esse é o valor total do salario com o bonus: ",salario)

else:
    salario = salariodoVendedor + 1000.00 
    print('Esse é o valor total do salario com o bonus:', salario)