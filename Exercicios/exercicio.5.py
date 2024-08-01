#Calculadora IMC: Crie uma função que receba dois parâmetros que
# serão o peso e a altura de uma pessoa e retorne seu IMC.

def imc(peso, altura):
    resultado = peso / (altura * altura)
    return resultado

def peso_ideal(imc):
    if imc <= 18.5:
        print("magreza")
    elif imc > 18.5 and imc < 24.9:
        print("sobrepeso")
    elif imc > 29.9 and imc < 39.9:
        print("obesidade")
    elif imc > 39.9:
        print("obesidade grave")

peso = float(input("Dgite o seu peso: "))
altura = float(input("Dgite sua altura: "))

imc = imc(peso, altura)
peso_ideal(imc)