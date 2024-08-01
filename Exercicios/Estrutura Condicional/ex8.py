# While: Esta executando uma repetição
while True:
    # Try: O try vai tentar executa esse bloco de codigo
    try:
        # Int: O int ser para colocar número inteiro
        # Input: O input serve para entrada de valores
        renda = float(input('Digite a sua renda mensal: '))

        # If: O if vai executa o código
        if renda > 1000 and renda <= 56.072:
            resposta = 0
        # Elif: O elif vai executa, se o if não executa
        elif renda > 56072.01 and renda <= 238.532:
            resposta = 7.50
        elif renda > 238532.01 and renda <= 522.400:
            resposta = 15
        elif renda > 522400.01 and renda <= 987.600:
            resposta = 22.50
        elif renda > 987.600:
            resposta = 27.50
        # Else: O else vai executa, se o if e elif não executar
        else:
            # Print: O print serve para mostrar um texto
            print('invalido')
        # Variavel: Um local para armazenar uma informação
        porcentagem = (renda * resposta) / 100
        print(f'Essa quantia sera descontada: {porcentagem}')
    # Except: Se não funcionar o try, vai executa o except
    except ValueError:
        print('Esta errado, coloque sua renda')


