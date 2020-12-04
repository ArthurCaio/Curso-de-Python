maior = 0
menor = 100
for c in range (0,5):
    peso = float(input('Digite o peso: '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('o menor peso é {} \ne o maior peso é {}'.format(menor,maior))
