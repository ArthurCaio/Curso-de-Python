import random
itens = ('PEDRA','PAPEL','TESOURA')
print('[ 1 ] PEDRA')
print('[ 2 ] PAPEL')
print('[ 3 ] TESOURA')
jogada = int(input('Qual a sua jogada: '))-1
com = random.randint(0,2)
print('JO!')
print('KEN!')
print('PO!')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('Você escolheu {}.'.format(itens[jogada]))
print('O Computador escolheu {}.'.format(itens[com]))
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
if jogada == 0 and com == 2:
    print('VOCÊ GANHOU!')
elif jogada == 1 and com == 0:
    print('VOCÊ GANHOU!')
elif jogada == 2 and com == 1:
    print('VOCÊ GANHOU!')
elif jogada == com:
    print('EMPATE!')
elif jogada == 0 and com == 1:
    print('VOCÊ PERDEU!')
elif jogada == 1 and com == 2:
    print('VOCÊ PERDEU!')
elif jogada == 2 and com == 0:
    print('VOCÊ PERDEU!')
