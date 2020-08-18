km = float(input('Digite Quantos Quilometros de Distancia é a Sua Viagem: '))
if km <= 200:
    p = km * 0.50
    print('Sua Viagem Vai Custa: {}'.format(p))
else:
    p = km * 0.45
    print('Sua Viagem Vai Custar: {}'.format(p))
print('Fim do Programa...')