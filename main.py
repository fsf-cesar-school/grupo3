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
    print("» Opção inválida.")

# •*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*
