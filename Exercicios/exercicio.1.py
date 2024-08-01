from datetime import datetime

def solicita_nome():
    # Input: O input serve para entrada de valores
    nome = input('Digite seu nome: ')
    return nome

def define_saudacao(hora_atual):
    # If: O if vai executa o código
    if hora_atual >= 0 and hora_atual <= 5:
        # Variavel: Um local para armazenar uma informação
        saudacao = 'Boa Madrugada'
    elif hora_atual <= 12:
        saudacao = 'Bom Dia'
    #  Elif: O elif vai executa, se o if não executa
    elif hora_atual <= 19:
        saudacao = 'Boa Tarde'
    # Else: O else vai executa, se o if e elif não executar
    else:
        saudacao = 'Boa Noite'

    return saudacao


def exibir_mensagem(nome, saudacao):
    # Print: O print serve para mostrar um texto
    print(saudacao + nome)

# Variavel: Um local para armazenar uma informação
exibir_mensagem(solicita_nome(), define_saudacao(datetime.now().hour))