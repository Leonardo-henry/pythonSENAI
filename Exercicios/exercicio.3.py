from datetime import datetime

def menu_calculadora():
    print('Menu Calculadora')
    print('-=-=-=-=-=-=-=-=')
    print('1- Adição')
    print('2- Subtração')
    print('3- Multiplicacao')
    print('4- Divisão')
    print('-=-=-=-=-=-=-=-=')

def escolha_numero():
    while True:
        try:
            numero1 = int(input('Coloque um numero: '))
            return numero1
        except ValueError:
            print('Esta errado, tente novamente.')
def outro_numero():
    while True:
        try:
            numero2 = int(input('Coloque outro numero: '))
            return numero2
        except ValueError:
            print('Esta errado, tente novamente.')
def solicite_escolha():
    while True:
        try:
            escolha = int(input('Escolha entre 1 , 2 , 3 ou 4: '))
            return escolha
        except ValueError:
            print('Esta errado, tente novamente.')

def soma(numero1, numero2):
    soma = numero1 + numero2
    return soma

def subtracao(numero1, numero2):
    sub = numero1 - numero2
    return sub

def multiplicacao(numero1, numero2):
    multiplicacao = numero1 * numero2
    return multiplicacao

def divisao(numero1, numero2):
    divisao = numero1 / numero2
    return divisao

valor_a = escolha_numero()
valor_b = outro_numero()
menu_calculadora()
opcao = solicite_escolha()

if opcao == 1:
    print(valor_a + valor_b)
elif opcao == 2:
    print(valor_a - valor_b)
elif opcao == 3:
    print(valor_a * valor_b)
elif opcao == 4:
    print(valor_a / valor_b)

