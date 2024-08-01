def menu_calculadora():
    print("1 - tensao")
    print("2 - corrente")
    print("3 - resistencia")
    print("4 - resistencia resistor")
    menu1=(" tensao da fonte")
    menu2=(" tensao do led")
    menu3=(" corrente do led")
    return menu1+menu2+menu3


def conta1():
    if conta=="1":
        corrente=int(input("Qual a corrente: "))
        resistencia=int(input("Qual a resistencia: "))
        resultado_final=resistencia*corrente
        print("O resultado final é",resultado_final,"V")

    elif conta=="2":
        resistencia=int(input("Qual a resistencia: "))
        tensao=int(input("Qual a tensao: "))
        resultado_final=tensao/resistencia
        print("O resultado final é",resultado_final,"A")

    elif conta=="3":
        tensao=int(input("Qual a tensao: "))
        corrente=int(input("Qual a corrente: "))
        resultado_final=tensao/corrente
        print("O resultado final é",resultado_final,"Ω")

    elif conta=="4":
        tensao_fonte=int(input("Qual a tensao da fonte: "))
        tensao_led=int(input("Qual a tensao do led: "))
        corrente_led=int(input("Qual a corrente do led: "))
        resultado_final=(tensao_fonte-tensao_led)/corrente_led
        print("O resultado final é",resultado_final,"Ω")


menu_calculadora()
conta=input("digite qual das opções você gostaria: ")
conta1()
