
mensagem = print("Essa é uma Calculadora da Lei de Ohm e suas opções de calculos são: \nA-Tensão \nB-Corrente \nC-Resistencia \nD-Resistência Resistor")

conta = input("digite qual das opções você gostaria: ")
Z = "sair"
A = "tensao"
B = "corrente"
C = "resistencia"
D = "resistencia_resistor"
E = "tensao_fonte"
F = "tensao_led"
G = "corrente_led"

while conta != Z:

    if conta == "A":
        corrente = int(input("Qual a corrente: "))
        resistencia = int(input("Qual a resistencia: "))
        resultado_final = resistencia * corrente
        print("O resultado final é", resultado_final,"V")

    elif conta == "B":
        resistencia = int(input("Qual a resistencia: "))
        tensao = int(input("Qual a tensao: "))
        resultado_final = tensao / resistencia
        print("O resultado final é", resultado_final,"A")

    elif conta == "C":
        tensao = int(input("Qual a tensao: "))
        corrente = int(input("Qual a corrente: "))
        resultado_final = tensao / corrente
        print("O resultado final é", resultado_final,"Ω")

    elif conta == "D":
        tensao_fonte = int(input("Qual a tensao da fonte: "))
        tensao_led = int(input("Qual a tensao do led: "))
        corrente_led = int(input("Qual a corrente do led: "))
        resultado_final = (tensao_fonte - tensao_led) / corrente_led
        print("O resultado final é", resultado_final,"Ω")
