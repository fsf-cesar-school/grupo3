"""              APP CONTROL GLIC !              """

# •*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*

class Usuario:
    def __init__(self, nome, idade, email, telefone, endereco):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone
        self.endereco = endereco

# •*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*

    def exibir_perfil(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Email: {self.email}")
        print(f"Telefone: {self.telefone}")
        print(f"Endereço: {self.endereco}")

# •*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*

    @staticmethod # "o staticmethod é uma função de uma classe que interage de alguma forma com o objeto"
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
                    endereco = input("» Digite seu endereço: ")
                    print("» Perfil criado com sucesso!")
                    
                    Usuario.usuario_atual = Usuario(nome, idade, useremail, telefone, endereco)

                    return True
                else:
                    print("» As senhas não coincidem.")
                    return False

# •*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*

    @staticmethod
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

def tela_inicial():
    while True:
        escolhaentrada = int(input("» O que deseja fazer?\n1 → Cadastro\n2 → Login\n"))
        if escolhaentrada == 1:
            if Usuario.cadastro():
                break
        elif escolhaentrada == 2:
            if Usuario.login():
                break
        else:
            print("» Opção inválida.")

# •*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*

cafedamanha = []
almoco = []
janta = []
lanche = []

def alimentacao():
    print("» Aqui é onde você registrará as suas refeições diárias.")

    escolhaalimentacao = int(input("» Em qual das seguintes refeições você deseja implementar alimentos?\n1 → Café da manhã\n2 → Almoço\n3 → Jantar\n4 → Lanche"))
    
    while True:
        with open('comida.txt', 'r+') as f:
            if escolhaalimentacao == 1:
                comida = input("» O que você comeu no café da manhã? (Digite 'sair' para terminar)\n")
                if comida.lower() == "sair":
                    break
                f.write(f'- Café da manhã: {comida}')
                cafedamanha.append(comida)

            elif escolhaalimentacao == 2:
                comida = input("» O que você comeu no almoço? (Digite 'sair' para terminar)\n")
                if comida.lower() == "sair":
                    break
                f.write(f'- Almoço: {comida}')
                almoco.append(comida)

            elif escolhaalimentacao == 3:
                comida = input("» O que você comeu no jantar? (Digite 'sair' para terminar)\n")
                if comida.lower() == "sair":
                    break
                f.write(f'- Janta: {comida}')
                janta.append(comida)
                
            elif escolhaalimentacao == 4:
                comida = input("» O que você comeu no lanche? (Digite 'sair' para terminar)\n")
                if comida.lower() == "sair":
                    break
                f.write(f'- Lanche: {comida}')
                lanche.append(comida)
            else:
                print("» Opção inválida.")
                break

def listacomidas():
    print(f'Café da manhã: {cafedamanha}\nAlmoço: {almoco}\nJanta: {janta}\nLanche: {lanche}')

# •*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*

def tela_principal():
    while True:
        escolhaprincipal = int(input("» O que deseja fazer agora?\n1 → Controle da alimentação\n2 → Exibir perfil\n3 → Lista comidas\n4 -> Outro\n"))
        if escolhaprincipal == 1:
            alimentacao()
            break
        elif escolhaprincipal == 2:
            if hasattr(Usuario, 'usuario_atual') and Usuario.usuario_atual is not None:
                Usuario.usuario_atual.exibir_perfil()
            else:
                print("» Nenhum perfil para exibir. Por favor, faça o login ou cadastro primeiro.")
            break
        elif escolhaprincipal == 3:
            listacomidas()
            break
        elif escolhaprincipal == 4:
            print("» Opa, não está pronto ainda! Volte mais tarde.")
            break
        else:
            print("» Opção inválida.")

# •*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*

Usuario.usuario_atual = None

# •*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*

tela_inicial()
tela_principal()
