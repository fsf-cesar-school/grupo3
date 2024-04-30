"""              APP CONTROL GLIC !              """

# •*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*

users = open('users.txt', 'a')

# •*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*

def cadastro():
    useremail = input("» Insira o seu endereço de email:\n")
    userpassword = input("» Crie uma senha:\n")
    confirmpassword = input("» Confirme a sua senha:\n")

    with open('users.txt', 'r') as f:
        if useremail in f.read():
            print('» Esse email já está sendo utilizado.')
            return False
        else:
            if confirmpassword == userpassword:
                with open('users.txt', 'a') as f:
                    f.write(f'{useremail} {userpassword}\n')
                print('» Cadastro efetuado com sucesso!')

                nome = input("» Digite seu nome: ")
                idade = input("» Digite sua idade: ")
                telefone = input("» Digite seu telefone: ")
                endereço = input("» Digite seu endereço: ")
                print("Perfil criado com sucesso!")

                return True
            else:
                print("» As senhas não coincidem.")
                return False

### EDSON v

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

# •*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*

def login():
    userlogin = input("» Insira o seu endereço de email:\n")
    userpwd = input("» Insira sua senha:\n")

    with open('users.txt', 'r') as f:
        if userlogin in f.read():
            f.seek(0)
            for line in f:
                email, pwd = line.split()
                if userlogin == email and userpwd == pwd:
                    print("» Login efetuado com sucesso.")
                    return True
            print("» Senha incorreta.")
            return False
        else:
            print("» Endereço de email não cadastrado.")
            return False

# •*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*

        # TELA DE INÍCIO - CADASTRO/LOGIN #

def tela_inicial():
    while True:
        escolhaentrada = int(input("» O que deseja fazer?\n1 → Cadastro\n2 → Login\n"))
        if escolhaentrada == 1:
            if cadastro():
                break
        elif escolhaentrada == 2:
            if login():
                break
        else:
            print("» Opção inválida.")

# •*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*

def alimentacao():
    print("Aqui é onde você registrará as suas refeições diárias.")

    cafedamanha = []
    almoco = []
    janta = []

    escolhaalimentacao = int(input("» Em qual das seguintes refeições você deseja implementar alimentos?\n1 → Café da manhã\n2 → Almoço\n3 → Jantar\n"))
    
    while True:
        if escolhaalimentacao == 1:
            comida = input("» O que você comeu no café da manhã? (Digite 'sair' para terminar)\n")
            if comida.lower() == "sair":
                break
            cafedamanha.append(comida)

        elif escolhaalimentacao == 2:
            comida = input("» O que você comeu no almoço? (Digite 'sair' para terminar)\n")
            if comida.lower() == "sair":
                break
            almoco.append(comida)

        elif escolhaalimentacao == 3:
            comida = input("» O que você comeu no jantar? (Digite 'sair' para terminar)\n")
            if comida.lower() == "sair":
                break
            janta.append(comida)
        else:
            print("Opa, n ta pronto ainda")
            break

# •*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*

        # TELA PRINCIPAL #

def tela_principal():
    while True:
        escolhaprincipal = int(input("» O que deseja fazer agora?\n1 → Controle da alimentação\n2 → Exibir perfil\n"))
        if escolhaprincipal == 1:
            alimentacao()
            break
        elif escolhaprincipal == 2:
            exibir_perfil()
            break
        else:
            print("» Opção inválida.")

# •*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*

tela_inicial()
tela_principal()
