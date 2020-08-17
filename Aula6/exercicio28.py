import random
ran = random.randint(1,5)
no = str(input('Digite o Seu nome: '))
nu = int(input('Digite um numero de 1 ate 5: '))
if nu == ran:
    print('Parabêns {} Você Ganhou.'.format(no))
else:
    print('Você Perdeu')
    print('O Numero era {}'.format(ran))
print('Fim do programa...')