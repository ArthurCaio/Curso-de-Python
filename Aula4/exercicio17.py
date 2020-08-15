import math
co = float(input('Digite o Valor do Cateto Oposto: '))
ca = float(input('Digite o Valor do Cateto Adjacente: '))
hi = math.hypot(co,ca)
print('O valor da Hipotenusa é {:.2f}'.format(hi))