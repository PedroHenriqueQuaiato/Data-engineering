import time
import matplotlib
import numpy
import psycopg2


def conec ():
    host = 'localhost'
    user = 'postgres'
    password = 'postgres'
    port = '5434'
    db_name = 'rodrigo'
    return f"host={host} user={user} password={password} port={port} dbname={db_name}"

conn = psycopg2.connect (conec())
cur = conn.cursor()


class produção:
    def __init__(self, materia_prima, percentual_de_perda,produto,NFCe,MDFe,quantidade):
        self.materia_prima = materia_prima
        self.percentual_de_perda = percentual_de_perda
        self.produto = produto 
        self.NFCe = NFCe
        self.MDFe = MDFe
        self.quantidade = quantidade 

materia_prima = input('Qual materia prima utilizada:')
quantidade = int(input('Qual a quantidade de materia prima: '))
percentual_de_perda = int(input('Qual o percentual de perda: '))
produto = input('Qual o produto: ')
NFCe = int(input('Qual o numero do NFC-e: '))
MDFe = int(input('Qual o numero do MDF-e: '))

cadastro = produção(materia_prima = materia_prima, percentual_de_perda = percentual_de_perda, produto = produto, NFCe = NFCe, MDFe = MDFe, quantidade = quantidade )

def percent (percentual_de_perda, quantidade):
    per = percentual_de_perda / 100
    global tol 
    percentual_de_perda1 = quantidade * per 


percent(percentual_de_perda, quantidade)

cur.execute(
    "INSERT INTO produtos (materia_prima, quantidade, percentual_de_perda1, produto, NFCe, MDFe) VALUES (%s, %s, %s, %s, %s, %s)",
    produto
)
conn.commit()




