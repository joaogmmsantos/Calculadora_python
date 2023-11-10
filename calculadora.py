def calcular():
    operation = input('''
Por favor, digite a operação matemática que você deseja concluir:
+ para Adição
- para subtração
* para multiplicação
/ para divisão
''')

    number_1 = int(input('Insira seu primeiro número: '))
    number_2 = int(input('Insira o seu segundo número: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else: 
        print('Você não digitou um operador válido, execute o programa novamente.')

    novamente()

def novamente():
    calcular_novamente = input('''
Quer calcular novamente?
Digite S para SIM ou N para NÃO.
''')

    if calcular_novamente.upper() == 'S':
        calcular()
    elif calcular_novamente.upper() == 'N':
        print('Até mais.')
    else:
        novamente()

# Chame a função calcular() para iniciar o programa
calcular()
