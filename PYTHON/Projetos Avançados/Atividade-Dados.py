import pandas as pd 
import openpyxl as opx

arquivo = pd.read_csv(r"C:\Users\pedro\Downloads\AMZN.csv")

arquivo = arquivo.query("'2000-01-01' < Date < '2000-01-31'")  # deve se colocar a primeira data depois o nome do capo e depois a segunda data

arquivo ['Low'] = arquivo['Low'].round(2)
arquivo ['Open'] = arquivo['Open'].round(2)    # Setar o tamanho de casas decimasis dos resultados do data frame
arquivo ['High'] = arquivo['High'].round(2)
arquivo ['Close'] = arquivo['Close'].round(2)
arquivo ['Adj Close'] = arquivo['Adj Close'].round(2)


volume = arquivo['Volume']
open = arquivo['Open']

def soma (volume,open,arquivo):
    resut = open + volume 
    arquivo['Soma de Volume com abertura'] = resut

soma(volume,open,arquivo)

arquivo = arquivo.to_excel(r"C:\Users\pedro\Downloads\Amazon.xlsx")
arquivo.to_excel("C:\Users\pedro\Downloads\Amazon.xlsx", index=False)  # O parâmetro index=False evita que o índice do DataFrame seja salvo no arquivo

