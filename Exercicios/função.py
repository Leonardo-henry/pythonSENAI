from datetime import datetime

def menu_calculadora():
    print("Calculadora")
    print("1 - Adição")
    print("2 - Subtracao")
    print("3 - Multiplicacao")
    print("4 - Divisao")

# Exibe o menu da calculadora
menu_calculadora()

def ola_nome(nome):
    print(f"Ola {nome}")


def return_ola_name(nome):
    return f"Ola {nome}"

# Exibe o print com "Ola Leo"
ola_nome("Leo")

# Retorna o texto com o "Ola Leo"
print("Boa tarde return", return_ola_name("Leo"))

ola_nome("leo")

def calcular_idade(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade

def exibir_idade(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    print("A sua idade é", idade, "anos")

def solicita_ano_nascimento():
    while True:
        try:
            ano_nascimento = int(input("Digite seu ano de nascimento: "))
            if ano_nascimento > datetime.now().year:
                print("Digite um ano valido")
            else:
                return ano_nascimento
        except ValueError:
            print("Digite um valor inteiro. Ex: 1997")

# print(calcular_idade(ano_nascimento = 1997))

# exibir_idade(1997)

ano_nascimento = solicita_ano_nascimento()

exibir_idade(ano_nascimento = ano_nascimento)

print("A sua idade é", calcular_idade(ano_nascimento = 2007), "anos")

exibir_idade(2007)

