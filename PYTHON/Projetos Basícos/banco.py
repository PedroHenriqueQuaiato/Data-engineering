#Simulação de Banco:
#Implemente um sistema simples de simulação bancária que permita aos clientes abrir contas, fazer depósitos, retiradas e consultar saldos.


class DadosPessoais:
    def __init__(self, nome, idade, endereço, cpf):
        self.nome = nome
        self.idade = idade
        self.endereço = endereço 
        self.cpf = cpf

    def retornar(self):
        print('Nome cadastrado:', self.nome)
        print('Idade cadastrada: ', self.idade)
        print('Endereço cadastrado: ', self.endereço)
        print('CPF cadastrado :', self.cpf)

pessoa = DadosPessoais(nome= input('Digite o seu nome: '), idade= int(input('Digite a sua idade: ')), 
                       endereço= input('Digite o seu endereço: '), cpf=int(input('Digite o seu CPF: ')))
pessoa.retornar()
    
        
