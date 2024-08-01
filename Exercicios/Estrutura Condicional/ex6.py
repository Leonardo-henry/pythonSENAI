# While: esta executando uma repetição
while True:
    # Try: O try vai tentar executa esse bloco de codigo
    try:
        # Int: O int ser para colocar número inteiro
        # Input: O input serve para entrada de valores
        numero = int(input('Digite o primeiro número: '))
        numero2 = int(input('Digite o segundo número: '))
        numero3 = int(input('Digite o terceiro número: '))
        # Variavel: Um local para armazenar uma informação
        resposta = ''

        # If: O if vai executa o código
        if numero > numero2 and numero > numero3:
            resposta = ('O primeiro número é maior')
        #  Elif: O elif vai executa, se o if não executa
        elif numero2 > numero and numero2 > numero3:
            resposta = ('O segundo número é maior')
        elif numero3 > numero and numero3 > numero2:
            resposta = ('O terceiro número é maior')
        # Else: O else vai executa, se o if e elif não executar
        else:
            # Print: O print serve para mostrar um texto
            print('invalido')
        print(resposta)
        # Except: Se não funcionar o try, vai executa o except
    except ValueError:
        print('Esta errado, coloque um número')