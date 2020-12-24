km = float(input('Digite Quantos Quilometros Por Hora Você Rodou: '))
if km > 80 :
    m = (km - 80) * 7
    print('Você Pagará Uma mulda de: R${:.2f} .'.format(m))
    print('Fim do Programa...')