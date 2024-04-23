#            APP CONTROL GLIC ! <<<<<<<<<<<<<<<<<<<<<<<<<,

users = open('users.txt', 'a')

#

def cadastro():
    useremail = input("Insira o seu email:\n")
    userpassword = input("Crie uma senha:\n")
    confirmpassword = input("Confirme a sua senha:\n")

    if useremail in 'users.txt':
        print('Esse email já está sendo utilizado.')
    else:
        if confirmpassword == userpassword:
            users.write('{}\n'.format(useremail, userpassword))
            print('Cadastro efetuado com sucesso!')
        else:
            print("As senhas não coincidem.")

def login():
    userlogin = input("Insira o seu email:\n")
    # INCOMPLETO !!

#

escolhaentrada = int(input("1 - > Cadastro\n2 - > Login\n"))
if escolhaentrada == 1:
    cadastro()
elif escolhaentrada == 2:
    login()
else:
    print("Opção inválida.")

#
