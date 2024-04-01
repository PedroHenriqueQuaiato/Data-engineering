def fibonacci(n):
    fibo = [0,1]
    while fibo[-1] + fibo[-2] <= n: # o -1 serve para acessar o ultimo numero do ARREY 
        fibo.append(fibo[-1] + fibo[-2])
    return fibo

fibo = fibonacci(100)
print(fibo)