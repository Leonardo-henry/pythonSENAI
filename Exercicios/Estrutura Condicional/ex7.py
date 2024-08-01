# While: Esta executando uma repetição
while True:
    # Try: O try vai tentar executa esse bloco de codigo
    try:
        # Int: O int ser para colocar número inteiro
        # Input: O input serve para entrada de valores
        mes = int(input('Digite um numero entre 1 a 12: '))
        # Variavel: Um local para armazenar uma informação
        h = 'Estamos no mês de'
        # If: O if vai executa o código
        if mes == 1:
            # Print: O print serve para mostrar um texto
            print(h, 'janeiro')
        # Elif: O elif vai executa, se o if não executa
        elif mes == 2:
            print(h, 'fevereiro')
        elif mes == 3:
            print(h, 'março')
        elif mes == 4:
            print(h, 'abril')
        elif mes == 5:
            print(h, 'maio')
        elif mes ==6:
            print(h, 'junho')
        elif mes == 7:
            print(h, 'julho')
        elif mes == 8:
            print(h, 'agosto')
        elif mes == 9:
            print(h, 'setembro')
        elif mes == 10:
            print(h, 'outubro')
        elif mes == 11:
            print(h, 'novembro')
        elif mes == 12:
            print(h, 'dezembro')
        # Else: O else vai executa, se o if e elif não executar
        else:
            # Raise: O raise força um erro
            raise TypeError
    except TypeError:
        print('Esta errado, coloque um número de 1 a 12')