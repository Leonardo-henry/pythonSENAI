import datetime

tempo = datetime.datetime.now()
mes = tempo.month
ano = tempo.year
dia = tempo.day
hora = tempo.hour
semana = datetime.datetime.now().isoweekday()
minuto = tempo.minute
segundo = tempo.second
resposta = ''
semana1 = ''

if mes == 1:
    resposta = 'janeiro'
elif mes == 2:
    resposta = 'fevereiro'
elif mes == 3:
    resposta = 'março'
elif mes == 4:
    resposta = 'abril'
elif mes == 5:
    resposta = 'maio'
elif mes == 6:
    resposta = 'junho'
elif mes == 7:
    resposta = 'julho'
elif mes == 8:
    resposta = 'agosto'
elif mes == 9:
    resposta = 'setembro'
elif mes == 10:
    resposta = 'outubro'
elif mes == 11:
    resposta = 'novembro'
elif mes == 12:
    resposta = 'dezembro'
else:
    print('erro')

if hora < 12:
    comprimento = "bom dia"
elif hora >= 12 and hora < 18:
    comprimento = "boa tarde"
else:
    comprimento = "boa noite"

if dia == 1:
    semana1 = 'segunda-feira'
elif dia == 2:
    semana1 = 'terça-feira'
elif dia == 3:
    semana1 = 'quarta-feira'
elif dia == 4:
    semana1 = 'quinta-feira'
elif dia == 5:
    semana1 = 'sexta-feira'
elif dia == 6:
    semana1 = 'sabado'
elif dia == 7:
    semana1 = 'domingo'

print(f"{comprimento}\nhoje é {semana1}, dia {dia} dos mês {mes} de {resposta} do ano {ano}, agora são {hora}:{minuto}:{segundo}")
