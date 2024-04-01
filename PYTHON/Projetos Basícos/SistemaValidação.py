class DadosPessoaisFisica:
    def __init__(self, nome, idade, cpf, sexo, profissao):
        self.nome = nome 
        self.idade = idade 
        self.cpf = cpf
        self.sexo = sexo 
        self.profissao = profissao

    def validar_idade(self):
        if self.idade >= 18:
            print('Idade válida para o cadastro!')
        elif 10 < self.idade < 18:
            print('Cadastro realizado com permissão de responsáveis.')
        else:
            print('Idade inválida!')

dados_pessoais = DadosPessoaisFisica(
    nome=input('Digite seu nome: '),
    idade=int(input('Digite sua idade: ')),
    cpf=int(input('Digite seu CPF: ')),
    sexo=input('Qual o seu sexo: '),
    profissao=input('Qual sua profissão: ')
)

dados_pessoais.validar_idade()

