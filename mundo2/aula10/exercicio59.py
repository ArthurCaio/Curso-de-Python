r = 0
n1 = 0
n2 = 0
while r != 5:
    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite outro numero: '))
    print('Escolha oque você quer fazer um numero.\n [1] - Soma\n [2] - Multiplicar \n [3] - Qual é o maior\n [4] - Novos Valores\n [5] - Enserrar programa')
    r = int(input('Resposta: '))
    if r == 1:
        print('{} + {} = {}'.format(n1,n2,n1+n2))
    elif r == 2:
        print('{} x {} = {}'.format(n1,n2,n1*n2))
    elif r == 3:
        if n1 > n2:
            print('O MAIOR VALOR É {}'.format(n1))
            print('E O MENOR VALOR É {}'.format(n2))
        elif n2 > n1:
            print('O MAIOR VALOR É {}'.format(n2))
            print('O MENOR VALOR É {}'.format(n1))