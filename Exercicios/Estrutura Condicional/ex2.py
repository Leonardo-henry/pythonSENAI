# While: esta executando uma repetição
while True:
    # Try: O try vai tentar executa esse bloco de codigo
    try:
        # Int: O int ser para colocar número inteiro
        # Input: O input serve para entrada de valores
        nota = int(input('Digite sua primeira nota: '))
        nota2 = int(input('Digite sua segunda nota: '))
        # Variavel: Um local para armazenar uma informação
        media = (nota + nota2) / 2

        # If: O if vai executa o código
        if media > 70:
            saudacao = 'Aprovado'
        #  Elif: O elif vai executa, se o if não executa
        elif media == 70:
            saudacao = 'Média'
        elif media < 70:
            saidacao = 'Reprovado'
        # Else: O else vai executa, se o if e elif não executar
        else:
            # Print: O print serve para mostrar um texto
            print('invalido')
        print(f'Devido sua média {media}, você esta {saudacao}')
    # Except: Se não funcionar o try, vai executa o except
    except ValueError:
        print('Esta errado, coloque sua nota')