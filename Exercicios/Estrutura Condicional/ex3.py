# While: esta executando uma repetição
while True:
    # Try: O try vai tentar executa esse bloco de codigo
    try:
        # Int: O int ser para colocar número inteiro
        # Input: O input serve para entrada de valores
        idade = int(input('Digite qual a sua idade: '))

        # If: O if vai executa o código
        if idade >= 18:
            print("você é maior de idade")
        #  Elif: O elif vai executa, se o if não executa
        elif idade < 18:
            # Print: O print serve para mostrar um texto
            print("você é menor de idade")
            # Raise: O raise força um erro
            raise TypeError
    # Except: Se não funcionar o try, vai executa o except
    except ValueError:
        print('Esta errado, coloque números')