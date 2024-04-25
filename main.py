"""              APP CONTROL GLIC !              """

# •*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*

users = open('users.txt', 'a')

# •*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*

def cadastro():
    useremail = input("» Insira o seu endereço de email:\n")
    userpassword = input("» Crie uma senha:\n")
    confirmpassword = input("» Confirme a sua senha:\n")

    if useremail in 'users.txt':
        print('» Esse email já está sendo utilizado.')
    else:
        if confirmpassword == userpassword:
            users.write(f'[{useremail, userpassword}]\n')
            print('» Cadastro efetuado com sucesso!')
        else:
            print("» As senhas não coincidem.")

# •*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*

def login():
    userlogin = input("» Insira o seu endereço de email:\n")
    open('users.txt', 'r')
    if userlogin in 'users.txt':
        userpwd = input("» Insira sua senha")
        if userpwd in 'users.txt':
            print("» Login efetuado com sucesso.")
        else:
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
