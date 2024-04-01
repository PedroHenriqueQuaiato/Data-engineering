class Pessoa:                            #Class serve para criar uma clase                        
    def __init__(self, nome, idade):     # a ideia de __init__ é como se fosse a função para construir minha classe, no caso tudo que tem em uma pessoa 
        self.nome = nome                 #o próprio nome da instância da classe". O nome é uma instancia e para chamar ele temos que usar SELF.
        self.idade = idade
        
    def getNome(self):                   #Aqui é uma segunda função para deixar mais forte minha classe, aqui só estou pegando meu nome
        return self.nome
        
emanoel = Pessoa("Emanoel", 28)
print(emanoel.getNome())

pedro = Pessoa("Pedro", 30)


#------------- HERANÇA -------------------

class Pessoa:                                 
    def __init__(self, nome, idade):    #é obrigatorio colocar o self 
        self.nome = nome                
        self.idade = idade
        
    def getNome(self):                   # função para retornar o nome 
        return self.nome
    
class PessoaJuridica(Pessoa):
    def __init__(self,nome,idade,CNPJ,nomefantasia):
        super().__init__ (nome, idade)                  #o SUPER(). seria para chamar a construção da classe pai (nesse caso classe pessoa)
        self.CNPJ = CNPJ
        self.nomefantasia = nomefantasia

#-----------------------------------------------------------------------------------------------------------------------------------------------------
class DadosPessoais:
    def __init__(self, nome, idade, endereço, cpf):
        self.nome = nome
        self.idade = idade
        self.endereço = endereço 
        self.cpf = cpf

    def retornar(self):
        print('Nome cadastrado', self.nome)
        print('Idade cadastrada: ', self.idade)
        print('Endereço cadastrado ', self.endereço)
        print('CPF cadastrado :', self.cpf)

pessoa = DadosPessoais(nome='Pedro', idade=16, endereço='Rua Felipe J', cpf=123456789)
pessoa.retornar()
