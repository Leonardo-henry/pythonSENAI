from random import randint #sortei número
sai = 'não'
print("Inciando o Jogo")
while sai == 'não':

    maquina = randint(0, 10)
    escolha = input("Digite sua escolha Par ou Impar [P/I]: ")
    lance = int(input("Escolha um numero: "))
    soma = lance + maquina
    resto = soma % 2
    print(f'voce jogou {lance} e o computador jogou {maquina}. Total de {soma}')
    print("")
    print("Deu Par" if soma % 2 == 0 else "Deu Impar")

    if resto == 0:
        print("voce venceu")
    else:
        print("voce perdeu")

    if escolha == "P":
        if soma % 2 == 0:
            print("voce venceu")
            v += 1
        else:
            print("voce perdeu")

    elif escolha == 'I':
        if soma % 2 == 1:
            print("voce venceu")
        else:
            print("voce perdeu")
    sai = input("deseja sair do jogo ?: ")

    if sai == 'sim':

        print("Fim de jogo")
        break








