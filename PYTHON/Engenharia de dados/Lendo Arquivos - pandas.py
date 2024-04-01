import pandas as pd 

# Lendo arquivos com o pandas ( CSV )

arquivo = pd.read_csv("Caminho do arquivo")

print(arquivo)

arquivo.head(5) # retorna os primeiros 5 do arquivo

arquivos = pd.read_csv('arquivos/customers.csv', index_col=0)
arquivos.head(5)

# Quando carregamos um CSV os indices são gerados aleatoriamente por ordem da linha 
# caso queiramos especificar um indice, precisaremos informar qual a coluna é o indice

# Lendo arquivos do EXEL 

arquivo = pd.read_excel('Caminhos do exel')

print(arquivo)

#lendo arquivos de HTML

arquivo = pd.read_html('Caminho do arquivo HTML')

print(arquivo)

# Lendo arquivos JSON 

arquivo = pd.read_json('Caminho do arquivo json', orient='records')

print(arquivo)

#records' indica que o arquivo JSON contém uma lista de registros, onde cada registro é representado como um dicionário.

# importar dados de uma URL

url = "https://api.exchangerate-api.com/v4/latest/USD"
arquivo = pd.read_csv(url) # com base na URL ou API vou buscar os dados e ler em forma de JSON
print(arquivo)

arquivo.to_csv("C:\\Users\\pedro\\OneDrive\\Área de Trabalho\\Curso engenharia de dados\\Projetos\\json.csv")
# Esse arquivo.to_csv é para salvar em um csv na pasta designada

# ------ Salvando Data Frame em JSON ou em CSV

df = pd.DataFrame([1,2,3])
print(df)
df.to_json("./arquivos/numeros_json.json") # Para salvar em JSON
df.to_csv("./arquivos/numeros_csv.json") # Para salvar em CSV

#------ CRIANDO CULUNAS -----------

df = pd.DataFrame([1,2,3,4,5], columns = ['Numeros']) #Crie uma coluna chamada numeros para os dados numericos
print(df)
df.to_json




