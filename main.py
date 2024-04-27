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
        else:
            if confirmpassword == userpassword:
                with open('users.txt', 'a') as f:
                    f.write(f'{useremail} {userpassword}\n')
                print('» Cadastro efetuado com sucesso!')
            else:
                print("» As senhas não coincidem.")

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
                    return
            print("» Senha incorreta.")
        else:
            print("» Endereço de email não cadastrado.")

# •*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*

        # TELA DE INÍCIO - CADASTRO/LOGIN #

escolhaentrada = int(input("» O que deseja fazer?\n1 → Cadastro\n2 → Login\n"))
if escolhaentrada == 1:
    cadastro()
elif escolhaentrada == 2:
    login()
else:
    print("» Opção inválida..")

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
            print("» Opa, n ta pronto ainda")
            break

# •*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*

        # TELA PRINCIPAL #

escolhaprincipal = int(input("» O que deseja fazer agora?\n1 → Controle da alimentação\n2 → etc\n"))
if escolhaprincipal == 1:
    alimentacao()
else:
    print("» Opa, n ta pronto ainda")

# •*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*
