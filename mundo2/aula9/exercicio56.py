idade = [0,0,0,0];
idadeh = 0
idadem =  0
for c in range (0,4):
    nome = str(input('Digite o seu nome: '))
    idade[c] = int(input('Digite a sua idade: '))
    print('Qual você escolhe')
    print('[1] - Mulher')
    print('[2] - Homem')
    sexo = int(input('Digite o seu sexo:'))
    if sexo == 2 and idade[c] >= idadeh:
        idadeh = idade[c]
    if sexo == 1 and idade[c] < 20:
        idadem += 1
media = (idade[0] + idade[1] + idade[2] + idade[3])/4
print('A media de idade das pessoas são {}'.format(media))
print('A idade do Homen mais velho é {}'.format(idadeh))
print('A {} mulheres menores de idade'.format(idadem))