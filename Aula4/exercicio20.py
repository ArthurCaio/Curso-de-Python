import random
n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))
li = [n1,n2,n3,n4]
random.shuffle(li)
print('a ordem paar apresentar o trabalho é {}'.format(li))