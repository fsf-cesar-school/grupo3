from datetime import datetime
import os


##### Cadastro das pessoas para contatos de urgência (envio de alertas)#####
############################################################################

contatos = []
i = 0
def pede_nome():
    nome = input("Nome: ")
    nome_formatado = f"Nome: {nome}"
    return nome_formatado

def pede_telefone():
  telefone = input("Telefone: ")
  telefone_formatado = f"Telefone: {telefone}"
  return telefone_formatado

def pede_idade(i):
  while True:
    i = int(input("Idade: "))
    idade_formatada = f"Idade: {i}"
    if i < 18:
      print("Desculpe, essa pessoa ainda não pode ser um contato de emergência por ser menor de idade.")
    else:
      return str(idade_formatada)

def pede_endereco():
  endereco = input("Endereço: ")
  endereco_formatado = f"Endereço: {endereco}"
  return endereco_formatado

def mostra_dados(nome, telefone, idade, endereco):
  print("%s  %s  %s  %s" % (nome, telefone, idade, endereco))

def pede_nome_arquivo():
  return(input("Nome do arquivo --colocar extensão .txt--: "))

def pede_nome_arquivo_sugestao():
  sugestao_nome_arquivo_contato = "contatos.txt"
  resposta_usuario = input("Deseja usar o nome sugerido '{}'? (S/N): ".format(sugestao_nome_arquivo_contato))
  if resposta_usuario.upper() == 'S':
      nome_arquivo = sugestao_nome_arquivo_contato
      return nome_arquivo
  elif resposta_usuario.upper() == 'N':
      nome_arquivo = pede_nome_arquivo()
      return nome_arquivo
  elif not nome_arquivo:
      print("Nome do arquivo não pode estar vazio.")
  return nome_arquivo

def criar_arquivo_sugestao_contatos():
  sugestao_nome_arquivo_contato = "contatos.txt"
  resposta_usuario = input("Deseja usar o nome sugerido '{}'? (S/N): ".format(sugestao_nome_arquivo_contato))
  
  if resposta_usuario.upper() == 'S':
      nome_arquivo = sugestao_nome_arquivo_contato
      if contatos != []:
        grava_contato(nome_arquivo)
  elif resposta_usuario.upper() == 'N':
      nome_arquivo = pede_nome_arquivo()
  elif not nome_arquivo:
      print("Nome do arquivo não pode estar vazio.")
      return
  elif os.path.exists(nome_arquivo):
      print("O arquivo '{}' já existe. Deseja sobrescrever? (S/N) ".format(nome_arquivo))
      op = input("Digite sua opção: ")
      if op.upper() == 'S':
        grava_contato(nome_arquivo)
        print("Arquivo '{}' sobreescrito com sucesso.".format(nome_arquivo))
      elif op.upper() == 'N':
        op = input("1 → Criar novo nome de arquivo\n2 → volta menu\nEscolha sua opção: ")
        if op == '1':
          nome_arquivo = pede_nome_arquivo()
          grava_contato(nome_arquivo)
          print("Arquivo '{}' criado com sucesso.".format(nome_arquivo))
        elif op == '2':
          print("Voltando ao Menu...")
  else:
      with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
          print("Arquivo '{}' criado com sucesso.".format(nome_arquivo))

def pesquisa(nome):
  mnome = nome.lower()
  for p, e in enumerate(contatos):
    if e[0].lower() == mnome:
      return p
  return None

def novo():
  global contatos
  if os.path.exists("contatos.txt"):
    carrega_lista_contatos()
  idade = pede_idade(i)
  nome = pede_nome()
  telefone = pede_telefone()
  endereco = pede_endereco()
  contatos.append([nome, telefone, idade, endereco])

def apaga():
  global contatos
  nome = pede_nome()
  p = pesquisa(nome)
  if p != None:
    del contatos[p]
  else:
    print("Nome não encontrado!")

def altera():
  p = pesquisa(pede_nome())
  if p != None:
    nome = contatos[p][0]
    telefone = contatos[p][1]
    idade = contatos[p][2]
    endereco = contatos[p][3]
    print("Encontrado:")
    mostra_dados(nome, telefone, idade, endereco)
    idade = pede_idade(i)
    nome = pede_nome()
    telefone = pede_telefone()
    endereco = pede_endereco()
    contatos[p] = [nome, telefone, idade, endereco]
  else:
    print("Nome não encontrado!")

def lista_pura():
  print("\nContatos\n\n------")
  for e in contatos:
    mostra_dados(e[0], e[1], e[2], e[3])
  print("------\n")

def lista():
  global contatos
  if not contatos:
    op = input("A lista está vazia, deseja carregar os contatos? (S/N) ")
    if op.upper() == 'S':
      carrega_lista_contatos()
      lista_pura()
    elif op.upper() == 'N':
      lista_pura()
  else:
    lista_pura()

def carrega_lista_contatos():
    global contatos
    nome_arquivo = pede_nome_arquivo_sugestao()
    arquivo = open(nome_arquivo, 'r', encoding='utf-8')
    contatos=[]
    for l in arquivo.readlines():
      nome, telefone, idade, endereco = l.strip().split(" || ")
      contatos.append([nome, telefone, idade, endereco])
      arquivo.close()

def carrega_lista_contatos_alertas():
    global contatos
    nome_arquivo = "contatos.txt"
    arquivo = open(nome_arquivo, 'r', encoding='utf-8')
    contatos=[]
    for l in arquivo.readlines():
      nome, telefone, idade, endereco = l.strip().split(" || ")
      contatos.append([nome, telefone, idade, endereco])
      arquivo.close()

def dispara_alerta():
  printar_lista_contatos_alertas()
  if os.path.exists("contatos.txt"):
    carrega_lista_contatos_alertas()
    lista_pura()
  else:
    printar_alerta_cadastro_contatos()

def grava_contato(nome_arquivo):
  arquivo = open(nome_arquivo, 'w', encoding='utf-8')
  for e in contatos:
    arquivo.write("%s || %s || %s || %s\n" % (e[0], e[1], e[2], e[3]))
  print("Contato(s) adicionado(s) no arquivo!")
  arquivo.close()

def grava_contatos():
    nome_arquivo = pede_nome_arquivo()
    if os.path.exists(nome_arquivo):
      op = print("Esse nome de arquivo já existe, se você continuar vai\nSOBREESCREVER as informações anteriores, caso deseje apenas\nacrescentar informações ao arquivo deverá carregar a lista:\n\n1 → Carregar lista\n2 → Sobreescrever\nEscolha uma opção: ")
      if op == '1':
        grava_contato(nome_arquivo)
      elif op == '2':
        carrega_lista_contatos()
        grava_contato(nome_arquivo)
    else:
      print("Opção inválida")

def validade_faixa_menu(pergunta, inicio, fim):
  while True:
    try:
      valor = int(input(pergunta))
      if inicio <= valor <= fim:
        return(valor)
      else:
        print("\n----------------------------------------------------------\nValor fora da faixa aceitável, favor digitar entre %d e %d\n----------------------------------------------------------\n" % (inicio, fim))
    except ValueError:
      print("\n---------------------------------------------\nValor inválido, favor digitar entre %d e %d\n---------------------------------------------\n" % (inicio, fim))


############################ Gráfico da glicemia ###########################
############################################################################

tabela_glicemia = []
tx_glicemia = "glicemia.txt"
glicemia = 0

def pede_glicemia():
  glic = float(input("Digite o valor da sua glicemia: "))
  #glic_formatada = f"Glicemia: {glic}"
  return glic

def data_atual():
  data_e_hora_atuais = datetime.now()
  data_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y')
  data_formatada = f"Data: {data_em_texto}"
  return data_formatada

def hora_atual():
  data_e_hora_atuais = datetime.now()
  hora_em_texto = data_e_hora_atuais.strftime('%H:%M')
  hora_formatada = f"Hora: {hora_em_texto}"
  return hora_formatada

def mostra_dados_glicemia(glicemia, data, hora):
  print("%s  %s  %s" % (glicemia, data, hora))

def lista_pura_glicemia():
  print("\nGlicemias\n\n------")
  for e in tabela_glicemia:
    mostra_dados_glicemia(e[0], e[1], e[2])
  print("------\n")

def grava_glicemia():
  nome_arquivo = tx_glicemia
  arquivo = open(nome_arquivo, 'w', encoding='utf-8')
  for e in tabela_glicemia:
    arquivo.write("%s || %s || %s\n" % (e[0], e[1], e[2]))
  print("Glicemia adicionada no arquivo!")
  arquivo.close()

def carrega_lista_glicemia():
    global tabela_glicemia
    nome_arquivo = tx_glicemia
    arquivo = open(nome_arquivo, 'r', encoding='utf-8')
    tabela_glicemia=[]
    for l in arquivo.readlines():
      glicemia, data, hora = l.strip().split(" || ")
      tabela_glicemia.append([glicemia, data, hora])
    arquivo.close()

def grava_glicemias():
    nome_arquivo = tx_glicemia
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for glicemia1, data, hora in tabela_glicemia:
            arquivo.write("%s || %s || %s\n" % (glicemia1, data, hora))
    print("Glicemia(s) gravada(s) com sucesso no arquivo '{}'.".format(nome_arquivo))

def verifica_existencia_arquivo():
  nome_arquivo = tx_glicemia
  if os.path.exists(nome_arquivo):
    carrega_lista_glicemia()
  return

def nova_inclusao_glicemia():
  global tabela_glicemia, glicemia
  verifica_existencia_arquivo()
  glicemia1 = f"Glicemia: {glicemia}"
  data = data_atual()
  hora = hora_atual()
  tabela_glicemia.append([glicemia1, data, hora])
  lista_pura_glicemia()

def analise_glicemia():
  global glicemia
  glicemia = pede_glicemia()
  if glicemia >= 70 and glicemia <= 110:
    print("Você está dentro da faixa aceitável de glicemia")
    nova_inclusao_glicemia()
    grava_glicemias()
  elif glicemia < 70:
    print(f"Você está em estado de hipoglicemia, sua glicemia foi de {glicemia}")
    dispara_alerta()
    nova_inclusao_glicemia()
    grava_glicemias()
  elif glicemia > 110 and glicemia <= 124:
    print(f"Você está em estado de hiperglicemia, sua glicemia foi de {glicemia}")
    nova_inclusao_glicemia()
    grava_glicemias()
  elif glicemia >= 125 and glicemia < 200:
    print(f"Você está dentro da faixa de diabetes, sua glicemia foi de {glicemia}")
    nova_inclusao_glicemia()
    grava_glicemias()
  elif glicemia >= 200:
    print(f"Você está em estado de emergência, sua glicemia foi de {glicemia}")
    dispara_alerta()
    nova_inclusao_glicemia()
    grava_glicemias()
  else:
    print("Valor inválido, tente novamente")


########################### Cadastro de lembretes ##########################
############################################################################

lembretes = []

def pede_nome_lembrete():
  titulo = input("Título do lembrete: ")
  titulo_formatado = f"Título: {titulo}"
  return titulo_formatado

def pede_lembrete():
  lembrete = input("Escreva o lembrete: ")
  lembrete_formatado = f"Lembrete: {lembrete}"
  return lembrete_formatado

def data_lembrete():
  data = input("Data: ")
  data_formatada = f"Data: {data}"
  return data_formatada

def hora_lembrete():
  hora = input("Hora: ")
  hora_formatada = f"Hora: {hora}"
  return hora_formatada

def mostra_dados_lembrete(nome_lembrete, pede_lembrete, data, hora):
  print("%s  %s  %s  %s" % (nome_lembrete, pede_lembrete, data, hora))

def pede_nome_arquivo_sugestao_lembrete():
  sugestao_nome_arquivo_lembrete = "lembretes.txt"
  resposta_usuario = input("Deseja usar o nome sugerido '{}'? (S/N): ".format(sugestao_nome_arquivo_lembrete))
  if resposta_usuario.upper() == 'S':
      nome_arquivo = sugestao_nome_arquivo_lembrete
      return nome_arquivo
  elif resposta_usuario.upper() == 'N':
      nome_arquivo = pede_nome_arquivo()
      return nome_arquivo
  elif not nome_arquivo:
      print("Nome do arquivo não pode estar vazio.")
  return nome_arquivo

def criar_arquivo_sugestao_lembretes():
  sugestao_nome_arquivo_contato = "lembretes.txt"
  resposta_usuario = input("Deseja usar o nome sugerido '{}'? (S/N): ".format(sugestao_nome_arquivo_contato))
  
  if resposta_usuario.upper() == 'S':
      nome_arquivo = sugestao_nome_arquivo_contato
      if lembretes != []:
        grava_lembrete(nome_arquivo)
  elif resposta_usuario.upper() == 'N':
      nome_arquivo = pede_nome_arquivo()
  elif not nome_arquivo:
      print("Nome do arquivo não pode estar vazio.")
      return
  elif os.path.exists(nome_arquivo):
      print("O arquivo '{}' já existe. Deseja sobrescrever? (S/N) ".format(nome_arquivo))
      op = input("Digite sua opção: ")
      if op.upper() == 'S':
        grava_lembrete(nome_arquivo)
        print("Arquivo '{}' sobreescrito com sucesso.".format(nome_arquivo))
      elif op.upper() == 'N':
        op = input("1 → Criar novo nome de arquivo\n2 → volta menu\nEscolha sua opção: ")
        if op == '1':
          nome_arquivo = pede_nome_arquivo_sugestao_lembrete()
          grava_lembrete(nome_arquivo)
          print("Arquivo '{}' criado com sucesso.".format(nome_arquivo))
        elif op == '2':
          print("Voltando ao Menu...")
  else:
      with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
          print("Arquivo '{}' criado com sucesso.".format(nome_arquivo))

def carrega_lista_lembretes():
    global lembretes
    nome_arquivo = pede_nome_arquivo_sugestao_lembrete()
    arquivo = open(nome_arquivo, 'r', encoding='utf-8')
    lembretes=[]
    for l in arquivo.readlines():
      nome_lembrete, pede_lembrete, data, hora = l.strip().split(" || ")
      lembretes.append([nome_lembrete, pede_lembrete, data, hora])
      arquivo.close()

def lista_pura_lembretes():
  print("\nLembretes\n\n------")
  for e in lembretes:
    mostra_dados_lembrete(e[0], e[1], e[2], e[3])
  print("------\n")

def lista_lembretes():
  global lembretes
  if not lembretes:
    op = input("A lista está vazia, deseja carregar os lembretes? (S/N) ")
    if op.upper() == 'S':
      carrega_lista_lembretes()
      lista_pura_lembretes()
    elif op.upper() == 'N':
      lista_pura_lembretes()
  else:
    lista_pura_lembretes()

def pesquisa_lembrete(nome):
  mnome = nome.lower()
  for p, e in enumerate(lembretes):
    if e[0].lower() == mnome:
      return p
  return None

def grava_lembrete(nome_arquivo):
  arquivo = open(nome_arquivo, 'w', encoding='utf-8')
  for e in lembretes:
    arquivo.write("%s || %s || %s || %s\n" % (e[0], e[1], e[2], e[3]))
  print("Lembrete(s) adicionado(s) no arquivo!")
  arquivo.close()

def grava_lembretes():
    nome_arquivo = "lembretes.txt"
    if os.path.exists(nome_arquivo):
      op = print("Esse nome de arquivo já existe, se você continuar vai\nSOBREESCREVER as informações anteriores, caso deseje apenas\nacrescentar informações ao arquivo deverá carregar a lista:\n\n1 → Sobreescrever\n2 → Carregar lista e gravar\nEscolha uma opção: ")
      if op == '1':
        grava_lembrete(nome_arquivo)
      elif op == '2':
        carrega_lista_lembretes()
        grava_lembrete(nome_arquivo)
    else:
      print("Opção inválida")

def novo_lembrete():
  global lembretes
  if os.path.exists("lembretes.txt"):
    carrega_lista_lembretes()
  nome_lembrete = pede_nome_lembrete()
  lembrete = pede_lembrete()
  data = data_lembrete()
  hora = hora_lembrete()
  lembretes.append([nome_lembrete, lembrete, data, hora])

def apaga_lembrete():
  global lembretes
  nome = pede_nome_lembrete()
  p = pesquisa_lembrete(nome)
  if p != None:
    del lembretes[p]
  else:
    print("Lembrete não encontrado!")

def altera_lembrete():
  p = pesquisa_lembrete(pede_nome_lembrete())
  if p != None:
    titulo_lembrete = lembretes[p][0]
    lembrete = lembretes[p][1]
    data = lembretes[p][2]
    hora = lembretes[p][3]
    print("Encontrado:")
    mostra_dados_lembrete(titulo_lembrete,lembrete, data, hora)
    titulo_lembrete = pede_nome_lembrete()
    lembrete = pede_lembrete()
    data = data_lembrete()
    hora = hora_lembrete()
    lembretes[p] = [titulo_lembrete, lembrete, data, hora]
  else:
    print("Nome não encontrado!")

################################### Menus ##################################
############################################################################

def menu_principal():
  print('''
  ---Menu Principal---
  
  1 → Gráfico de glicemia
  2 → Relatórios
  3 → Lembretes / Alarmes
  4 → Alimentação
  5 → Perfil
  0 → Sair
  ''')
  return validade_faixa_menu("Escolha uma opção: ", 0,5)

def menu_lembretes_alarmes():
  print('''
  ---Menu Lembretes / Alarmes---
  
  1 → Lembretes
  2 → Alarmes
  0 → Volta menu anterior
  ''')
  return validade_faixa_menu("Escolha uma opção: ", 0,2)

def menu_alarmes():
  print('''
  ---Menu Alarmes---
  
  1 → Novo contato
  2 → Altera contato
  3 → Apaga Contato
  4 → Lista Contatos
  5 → Grava em arquivos
  6 → Carregar arquivos
  0 → Volta menu anterior
  ''')
  return validade_faixa_menu("Escolha uma opção: ", 0,6)

def menu_lembretes():
  print('''
  ---Menu Lembretes---
  
  1 → Novo Lembrete
  2 → Altera Lembrete
  3 → Apaga Lembrete
  4 → Lista Lembretes
  5 → Grava em arquivos
  6 → Carregar arquivos
  0 → Volta menu anterior
  ''')
  return validade_faixa_menu("Escolha uma opção: ", 0,6)


############################################################################
# funções para os prints dos excepts:

def printar_valor_invalido():
  print("\n--------------\nValor inválido\n--------------\n")

def printar_arquivo_nao_encontrado():
  print("\n------------------------\nArquivo não encontrado!\n--------------------\n")

def todo():
  print("Ainda em desenvolvimento")

def printar_lista_contatos_alertas():
  print('''
  ##########################################################################
  ########## Enviando alerta para os seus contatos cadastrados!! ###########
  ##########################################################################
  ''')

def printar_alerta_cadastro_contatos():
  print('''
  ##########################################################################
  ########## ATENÇÃO, NENHUM CONTATO DE EMERGÊNCIA CADASTRADO !!! ##########
  ##########################################################################
  ''')

########################## Estrutura dos menus #############################
############################################################################

while True:
  try:
    opcao = menu_principal()
    if opcao == 0:
      break
    elif opcao == 1:
      #Gráfico de glicemias
      analise_glicemia()
    elif opcao == 2:
      #Relatórios
      todo()
    elif opcao == 3:
      while True:
        try:
          opcao = menu_lembretes_alarmes()
          if opcao == 0:
            break
          elif opcao == 1:
            #Lembretes
            while True:
              try:
                opcao = menu_lembretes()
                if opcao == 0:
                  break
                elif opcao == 1:
                  novo_lembrete()
                elif opcao == 2:
                  altera_lembrete()
                elif opcao == 3:
                  apaga_lembrete()
                elif opcao == 4:
                  lista_lembretes()
                elif opcao == 5:
                  criar_arquivo_sugestao_lembretes()
                elif opcao == 6:
                  carrega_lista_lembretes()
              except ValueError:
                printar_valor_invalido()
              except FileNotFoundError:
                printar_arquivo_nao_encontrado()
          elif opcao == 2:
            #Alarmes
            while True:
              try:
                opcao = menu_alarmes()
                if opcao == 0:
                  break
                elif opcao == 1:
                  novo()
                elif opcao == 2:
                  altera()
                elif opcao == 3:
                  apaga()
                elif opcao == 4:
                  lista()
                elif opcao == 5:
                  criar_arquivo_sugestao_contatos()
                elif opcao == 6:
                  carrega_lista_contatos()
              except ValueError:
                printar_valor_invalido()
              except FileNotFoundError:
                printar_arquivo_nao_encontrado()
        except ValueError:
          printar_valor_invalido()
        except FileNotFoundError:
          printar_arquivo_nao_encontrado()
    elif opcao == 4:
      #Alimentação
      todo()
    elif opcao == 5:
      #Perfil
      todo()
  except ValueError:
      printar_valor_invalido()
  except FileNotFoundError:
    printar_arquivo_nao_encontrado()
