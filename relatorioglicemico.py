"""Fazer relatório com opção de relatório diário, semanal e mensal
    - Nome do usuário:
        - ( Título - ex: Relatório Diário)
        - Níveis de Glicemia || Data || Hora
        
        ---
        
        - ( Título - ex: Relatório Semanal)
        - Níveis de Glicemia || Data || Hora"""

# RELATÓRIOS

def relatorio():
    niv_glicemia = input("Nível de glicemia: ")
    data_glic = input("Data: ")
    hora_glic = input("Horário: ")
    with open ('relatorio.txt', 'a+', encoding='utf-8') as fp:
        fp.write(f'Nível de Glicemia: {niv_glicemia} || Data: {data_glic} || Horário: {hora_glic}')

def print_relatorio():
    with open ('relatorio.txt', 'a+', encoding='utf-8') as fp:
        pr = fp.read()
    print(pr)

# chamar as funcões nos menus !!!
# tá funcionando :D
