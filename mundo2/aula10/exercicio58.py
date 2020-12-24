import random
numeroc = 0
numeroj = 1
numjo = 0
nome = input('Qual é o seu nome: ').upper()
while numeroc != numeroj:
    numeroc = random.randint(0,10)
    numeroj = int(input('Digite o numero entre 0 e 10: '))
    numjo += 1
    if numeroc == numeroj:
        print('PARABENS {} VOCÊ GANHOU!'.format(nome))
    else:
        print('VOCÊ PERDEU TENTE NOVAMENTE.')
print('Você preciso de {} para ganhar : )'.format(numjo))