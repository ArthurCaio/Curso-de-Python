media = 0
nh = ''
im =  0
ih = 0
for p in range (1,5):
    print('==== {}º PESSOA ===='.format(p))
    nome = str(input('Digite o seu nome: '))
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Sexo [M/F]:'))
    media += idade
    if sexo == 'M' and idade >= ih :
        ih = idade
        nh = nome
    if sexo == 'F' and idade < 20:
        im += 1
print('A media de idade das pessoas são {}'.format(media/4))
print('O nome do Homen mais velho é {}'.format(nh))
print('A {} mulheres menores de idade'.format(im))