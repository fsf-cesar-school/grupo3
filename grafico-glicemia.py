from datetime import datetime


glicemia = float(input("Digite o valor da sua glicemia: "))

if glicemia >= 70 and glicemia <= 110:
  print("Você está dentro da faixa aceitável de glicemia")
elif glicemia < 70:
  print(f"Você está em estado de hipoglicemia, sua glicemia foi de {glicemia}")
  print("Enviando alerta para os seus contatos cadastrados!!")
elif glicemia > 110 and glicemia <= 124:
  print(f"Você está em estado de hiperglicemia, sua glicemia foi de {glicemia}")
elif glicemia >= 125 and glicemia < 200:
  print(f"Você está dentro da faixa de diabetes, sua glicemia foi de {glicemia}")
elif glicemia >= 200:
  print(f"Você está em estado de emergência, sua glicemia foi de {glicemia}")
  print("Enviando alerta para os seus contatos cadastrados!!")
else:
  print("Valor inválido, tente novamente")


data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')

print(data_e_hora_em_texto) 