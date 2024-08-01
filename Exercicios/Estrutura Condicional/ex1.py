# While: esta executando uma repetição
while True:
    # Try: O try vai tentar executa esse bloco de codigo
    try:
        # Int: O int ser para colocar número inteiro
        # Input: O input serve para entrada de valores
        numero = int(input("digite um numero: "))
        # Variavel: Um local para armazenar uma informação
        p = 'positivo'
        n = 'negativo'
        nt = 'neutro'

        # If: O if vai executa o código
        if numero > 0:
            print('Devido esse número', numero,',então ele é', p)
        #  Elif: O elif vai executa, se o if não executa
        elif numero == 0:
            # Print: O print serve para mostrar um texto
            print('Devido esse número', numero,',então ele é', nt)
        elif numero < 0:
            print('Devido esse número', numero,'então ele é', n)
    # Except: Se não funcionar o try, vai executa o except
    except ValueError:
        print('Esta errado, coloque um número, Ex: 1')





