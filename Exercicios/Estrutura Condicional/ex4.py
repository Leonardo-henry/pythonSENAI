# While: esta executando uma repetição
while True:
    # Try: O try vai tentar executa esse bloco de codigo
    try:
        # Int: O int ser para colocar número inteiro
        # Input: O input serve para entrada de valores
        numero = int(input("Digite um numero: "))
        numero2 = int(input("Digite o segundo numero: "))

        # If: O if vai executa o código
        if numero > numero2:
            print ("O numero", numero,"é maior que o", numero2)
        #  Elif: O elif vai executa, se o if não executa
        elif numero < numero2:
            # Print: O print serve para mostrar um texto
            print("O numero", numero2,"é maior que o", numero)
    # Except: Se não funcionar o try, vai executa o except
    except ValueError:
        print('Esta errado, coloque sua renda')