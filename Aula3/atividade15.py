d = float(input('Quantos Dias Você Passou Com o Carro : '))
km = float(input('Quantos Quilometros Rodados : '))
d1 = d * 60 
km1 = km * 0.15
t = d1 + km1
print('O Total é {:.2f}R$ .'.format(t))