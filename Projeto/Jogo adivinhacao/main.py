from random import randint
sai = "não"
print('Iníciando Jogo')
while sai == 'não':
    random = randint(0, 100)
    chute = 0;
    chances = 10;
    while chute != random:
        chute = input('Chute um número entre 0 a 100: ')
        if chute.isnumeric():
            chute = int(chute)
            chances = chances - 1
            if chute == random:
                print('')
                print('Parabéns, você venceu! O número era {} e você ainda tinha {} chances.'.format(random, chances))
                print('')
                break;
            else:
                print('')
                if chute > random:
                    print('Você errou!!! Dica: É um número menor.')
                else:
                    print('Você errou!!! Dica: É um número maior.')
                print('Você tem ainda {} chances.'.format(chances))
                print('')
            if chances == 0:
                print('')
                print('Suas chances acabaram, você perdeu!')
                print('')
                break;
    sai = input("você deseja sair do jogo ?: ")

    if sai == 'sim':

        print('Fim do Jogo')
        break
