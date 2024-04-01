from validate_docbr import CPF

class Cadastro:
    def __init__(self, nome, idade, endereco, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.endereco = endereco

nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))
endereco = input('Digite o seu endereço: ')               
cpf = input('Digite o seu CPF: ')

pessoa = Cadastro(nome=nome, idade=idade, endereco=endereco, cpf=cpf)

def verificacao_cadastro(idade):
    if idade >= 18:
        print('Pode fazer o cadastro!')
    else:
        print('Não pode fazer o cadastro!')

verificacao_cadastro(pessoa.idade)

def valida_cpf(cpf):
    cpf_validator = CPF()
    if cpf_validator.validate(cpf):
        print('Este é um CPF válido!')
    else:
        print('Este é um CPF inválido!')


valida_cpf(pessoa.cpf)
