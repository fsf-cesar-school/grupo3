class Perfil:
    
    def __init__(self, nome, idade, email,telefone,endereço):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone
        self.endereço = endereço

    def exibir_perfil(self):
        
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"email: {self.email}")
        print(f"telefone: {self.telefone}")
        print(f"endereço: {self.endereço}")



# Solicitar ao usuário que insira seus dados para criar o perfil
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
email = input("Digite seu email: ")
telefone = input("Digite seu telefone: ")
endereço = input("Digite seu endereço: ")

print("Perfil criado com sucesso!")


