#O while repete tudo que esta dentro dele
while True:
    # O try vai tentar executa esse bloco de codigo
    try:
        idade = int(input('sua idade: '))

        # O if verifica se idade é valida
        if idade < 0 or idade > 100:
            print("idade ", idade)
            # O break sai do while
            break
        else:
            print("idade invalida")
    except ValueError:
        # Caso der erro executa aqui
        print("digite sua idade em numero. Ex: 26")
