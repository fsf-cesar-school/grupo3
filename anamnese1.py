def anamnese():
    global sexo, idade, altura, peso, imc, tipo_diabetes, terapia, unidades_medida, unidade_glicemia, hipoglicemia, glicemia_baixa, glicemia_desejada, glicemia_alta, hiperglicemia
    medicamentos = []
    dosagem = []
    dose_caneta = []
    bombas_insulina = []
    
    sexo_op = (input("Informe o seu sexo?\n(1) Feminino\n(2) Masculino\n(3) Prefiro não me identificar\n(4) Outro\nEscolha sua opção: "))
    if sexo_op == '1':
        sexo = 'Feminino'
    elif sexo_op == '2':
        sexo = 'Masculino'
    elif sexo_op == '3':
        sexo = 'Prefiro não me identificar'
    elif sexo_op == '4':
        sexo = 'Outro'
    
    idade = int(input("Informe sua idade: "))
    altura = float(input("Informe a sua altura: "))
    peso = float(input("Informe o seu peso: "))
    imc = peso/(altura*altura)
    
    diabetes_op = (input("Informe o tipo da sua Diabetes:\n(1) Tipo I\n(2) Tipo II\n(3) Gestacional\n(4) MODY\n(5) LADA\n(6) Outro\nEscolha sua opção: "))
    if diabetes_op == '1':
        tipo_diabetes = 'Tipo I'
    if diabetes_op == '2':
        tipo_diabetes = 'Tipo II'
    if diabetes_op == '3':
        tipo_diabetes = 'Gestacional'
    if diabetes_op == '4':
        tipo_diabetes = 'MODY'
    if diabetes_op == '5':
        tipo_diabetes = 'LADA'
    if diabetes_op == '6':
        tipo_diabetes = 'Outro'
    terapia_op = (input("Qual é a sua terapia?\n(1) Medicamento sem insulina\n(2) Injeções diárias\n(3) Bomba de insulina\n(4) Outra terapia\n(5) Não faz uso de terapia\nEscolha sua opção: "))
    if terapia_op == '1':
        terapia = 'Medicamento sem insulina'
        medicamentos.append(input("Qual o medicamento que você usa: "))
        dosagem.append(input("Qual a dosagem desse medicamento: "))
    elif terapia_op == '2':
        terapia = 'Injeções diárias'
        dose_caneta.append(input("Qual o aumento da dose de insulina na caneta: "))
    elif terapia_op == '3':
        terapia = 'Bomba de insulina'
        bombas_insulina.append(input("Qual a marca da Bomba de insulina: "))
    elif terapia_op == '4':
        terapia = 'Outra terapia'
        input("Informe qual outra terapia você utiliza: ")
    elif terapia_op == '5':
        terapia = 'Usuário não faz uso de terapia'
    else:
        print("Opção inválida!")
    unidades_medida_op = input("Especifique as unidades de medida:\n(1) US (lbs, oz, fl oz, inch)\n(2) Métrico (Kg, g, mL, cm)\nEscolha sua opção: ")
    if unidades_medida_op == '1':
        unidades_medida = 'US (lbs, oz, fl oz, inch)'
    elif unidades_medida_op == '2':
        unidades_medida = 'Métrico (kg, g, mL, cm)'
    unidade_glicemia_op = input("Qual a unidade que você mede sua glicemia:\n(1) mg/mL\n(2) mmol/L\nEscolha sua opção: ")
    if unidade_glicemia_op == '1':
        unidade_glicemia = 'mg/mL'
    elif unidade_glicemia_op == '2':
        unidade_glicemia = 'mmol/L'
    hipoglicemia = int(input("Informe o seu nível de hipoglicemia: "))
    glicemia_baixa = int(input('Informe o seu nível de glicemia baixa: '))
    glicemia_desejada = int(input('Informe o seu nível de glicemia desejada: '))
    glicemia_alta = int(input('Informe o seu nível de glicemia alta: '))
    hiperglicemia = int(input('Informe o seu nível de hiperglicemia: '))

def quadro_clinico():
    with open ('quadro_clinico.txt', 'a+', encoding='utf-8') as qc:
        qc.write(f"O seu quadro clínico é:\nSexo: {sexo}\nIdade: {idade} anos.\nAltura: {altura} m\nPeso: {peso} kg\nIMC: {imc:.2f}.\nTipo de Diabetes: {tipo_diabetes}\nTipo de terapia: {terapia}.\nSistema de medidas: {unidades_medida}\nUnd. Med. glicemia: ({unidade_glicemia}).\nMetas glicêmicas:\nHipoglicemia: {hipoglicemia}{unidade_glicemia}\nGlicemia baixa: {glicemia_baixa}{unidade_glicemia}\nGlicemia desejada: {glicemia_desejada}{unidade_glicemia}\nGlicemia alta: {glicemia_alta}{unidade_glicemia}\nHiperglicemia: {hiperglicemia}{unidade_glicemia}")

def print_quadro_clinico():
    with open ('quadro_clinico.txt', 'r', encoding='utf-8') as qdc:
        qdr_cln = qdc.read()
    print(qdr_cln)

anamnese()
quadro_clinico()
print_quadro_clinico()
