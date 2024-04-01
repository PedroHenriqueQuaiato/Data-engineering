import pandas as pd

arquivo = pd.read_csv(r"C:\Users\pedro\Downloads\Placement_Data_Full_Class.csv")

arquivo = arquivo.fillna("-")

def substituições (arquivo):
    arquivo['salary'] = arquivo['salary'].replace('-', '0.00')
    arquivo['ssc_b'] = arquivo['ssc_b'].replace('Others', 'Outros')

substituições(arquivo)

arquivo = arquivo.query("workex == 'Yes'")
arquivo = arquivo.query("hsc_s == 'Science'")
arquivo = arquivo.query("degree_t == 'Sci&Tech'")
arquivo = arquivo.query("specialisation == 'Mkt&HR'")
# Convertendo a coluna 'salary' para tipo numérico
arquivo['salary'] = arquivo['salary'].astype(float)
#o astype serve para mudar o tipo da coluna

# Aplicando a query após a conversão
arquivo = arquivo.query("salary > 250000.0")

arquivo = arquivo.to_csv("C:\\Users\\pedro\\OneDrive\\Área de Trabalho\\Curso engenharia de dados\\Projetos\\Atividade_2.csv")
