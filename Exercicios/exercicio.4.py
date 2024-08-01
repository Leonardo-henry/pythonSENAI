#Classificador de triangulo: Crie uma função que receba três números como parâmetros que
# serão os lados de um triângulo e retorne se ele é equilátero, isósceles ou escaleno.

def coloque_lado1():
    while True:
        try:
            lado1 = int(input('Coloque o valor do primairo lado: '))
            return lado1
        except ValueError:
            print('Esta errado, Tente Novamente')

def coloque_lado2():
    while True:
        try:
            lado2 = int(input('Coloque o valor do segundo lado: '))
            return lado2
        except ValueError:
            print('Esta errado, Tente Novamente')

def coloque_lado3():
    while True:
        try:
            lado3 = int(input('Coloque o valor do terceiro lado: '))
            return lado3
        except ValueError:
            print('Esta errado, Tente Novamente')

def verificar_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 and lado1 == lado3:
        return 'equilatero'
     elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
        return "escaleno"
    else:
        return 'isosceles'



lado1 = coloque_lado1()
lado2 = coloque_lado2()
lado3 = coloque_lado3()
resultado = verificar_triangulo(lado1, lado2, lado3)
print(f'O triangulo é {resultado}')