import datetime
mn = 0
mi = 0
at = datetime.date.today().year
for c in range (0,7):
    adn = int(input('Em que ano pessoa nasceu? '))
    idade = at - adn
    if idade >= 21:
        mi += 1
    else:
        mn += 1
print('Tem {} que são maiores de idade \nTem {} que são menores de idade.'.format(mi,mn))