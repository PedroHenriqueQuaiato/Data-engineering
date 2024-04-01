import pandas as pd

df = pd.read_csv('C:\\Users\\pedro\\Downloads\\4300Answers_femininos.csv')
print(df.head(5)) #checar as primeiras 5 conulas 

#Convertendo colunas NaN para '-'
df = df.fillna("-") #fillna serve para substituir arquivos NaN
print(df.head(5))
# Retonando Somente resultados Femininos

resultado_query = df.query("`Qual seu sexo?` == 'Feminino'")
resultado_query.head(2)
#A .quary serve para fazer uma quary no caso fiz desse modo: Coluna:
#Qual seu sexo deve ser == a 'Femino

resultado_query.to_csv("C:\\Users\\pedro\\OneDrive\\Área de Trabalho\\Curso engenharia de dados\\Projetos\\quary.csv")
#Salvei os arquivos na pasta do curso com o nome quanry 

# ---------- CRIAR TABELAS SQL COM O ARQUIVO --------

