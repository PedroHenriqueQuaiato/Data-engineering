import pandas as pd

df = pd.read_csv(r"C:\Users\pedro\Downloads\onlinefoods.csv")

df = df.query("Gender == 'Male'")  # quary para saber só os MACHOS

df = df.query("`Marital Status` == 'Married'")  # quando temos um nome de uma coluna que tem espaço temos que locar a crase para referenciar a coluna 


df['Monthly Income'] = df['Monthly Income'].replace('No Income', 'Sem Renda')  # aqui uso a função replace, que me ajuda a subtituir algum dado da coluna, por outr que eu queira
    # primeiro tenho que dizer qual coluna é, depois disseo coloco o nome da coluna em seguinda .replace, e depois coloco o que eu quero substituir pelo que eu quero colocar no lugar.

df['Monthly Income'] = df['Monthly Income'].replace('Below Rs.10000', 'Abaixo de 10.000 ')


df = df.sort_values(by ='Occupation', ascending=True)


print(df.head(20))

df = df.to_csv(r"C:\Users\pedro\OneDrive\Anexos\teste.csv")


    


