import random
n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))
li = [n1,n2,n3,n4]
print('Quem ira a pagar o quadro é {}'.format(random.choice(li)))