import matplotlib.pyplot as plt 
import numpy as np 


faturamento = {
    2000: 500000, 2001: 550000, 2002: 600000, 2003: 650000, 2004: 700000, 2005: 750000,
    2006: 800000, 2007: 850000, 2008: 900000, 2009: 950000, 2010: 1000000, 2011: 1050000,
    2012: 1100000, 2013: 1150000, 2014: 1200000, 2015: 1250000, 2016: 1300000, 2017: 1350000,
    2018: 1400000, 2019: 1450000, 2020: 1500000, 2021: 1550000, 2022: 1600000, 2023: 1650000,
    2024: 1700000,
}

anos = []
anos1 = []
valor = []

anos_analise = int(input('Escolha um ano para analise: '))
anos_analise1 = int(input('Escolha o segundo ano para analise: '))


for an in faturamento:
    global ano
    ano = an[anos_analise]
    anos.append(ano)

for f in faturamento:
    global ano2
    anos2 = f[anos_analise1]
    anos1.append(anos2)