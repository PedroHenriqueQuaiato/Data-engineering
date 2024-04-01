import tkinter as Tk
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="Realize seu cadastro !").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=100)


root.mainloop()

class Cadastro:
    def __init__(self,nome,idade,cpf,endereco):
        self.nome = nome 
        self.idade = idade 
        self.cpf = cpf
        self.endereco = endereco 

nome = input("Digite seu nome: ")
idade = int(input('Digite sua idade: '))
cpf = int(input("Digite o seu CPF: "))
endereco = input('Digite seu endereço: ')

nome = Tk.Entry(width=30)