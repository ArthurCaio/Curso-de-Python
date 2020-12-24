pro = float(input('Qual o valor do produto: '))
print('Você quer pagar como?')
print('1 - A Vista Dinheiro')
print('2 - A Vista no Cartão')
print('3 - em ate 2x no cartão')
print('4 - 3x ou mais no cartão')
r = int(input(''))
if r == 1:
    pro = pro - ((pro * 10)/100)
    print('Você vai pagar R${:.2f}'.format(pro))
elif r == 2:
    pro = pro - ((pro * 5)/100)
    print('Você vai pagar R${:.2f}'.format(pro))
elif r == 3:
    div = pro / 2
    print('Você vai pagar 2 parcelas de {:.2f}'.format(div))
elif r == 4:
    pro = pro + ((pro * 20)/100)
    p = int(input('Quantas parcelas? '))
    div = pro / p
    print('Você vai pagar {} parcelas de {:.2f}'.format(p,div))