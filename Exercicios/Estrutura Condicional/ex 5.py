# While: esta executando uma repetição
while True:
    # Try: O try vai tentar executa esse bloco de codigo
    try:
        # Int: O int ser para colocar número inteiro
        # Input: O input serve para entrada de valores
        dia = int(input('Digite um número de 1 a 7: '))
        # Variavel: Um local para armazenar uma informação
        h = 'hoje é'

        # If: O if vai executa o código
        if dia == 1:
            print(h, 'segunda-feira')
        #  Elif: O elif vai executa, se o if não executa
        elif dia == 2:
            print(h, 'terça-feira')
        elif dia == 3:
            print(h, 'quarta-feira')
        elif dia == 4:
            print(h, 'quinta-feira')
        elif dia == 5:
            print(h, 'sexta-feira')
        elif dia == 6:
            print(h, 'sabado')
        elif dia == 7:
            print(h ,'domingo')
        # Else: O else vai executa, se o if e elif não executar
        else:
            # Print: O print serve para mostrar um texto
            print('Número inválido. Digite um número de 1 a 7')
    # Except: Se não funcionar o try, vai executa o except
    except ValueError:
        print('Esta errado, coloque o número de 1 a 7')
