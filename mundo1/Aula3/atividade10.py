r = float(input('Digite Quanto Você Tem em Dinheiro : '))
d = float(input('Digite Qual o Valor do Dolar : '))
e = float(input('Digite Qual o Valor do Euro : '))
d1 = r / d
e1 = r / e
print('Você Tem {:.2f}U$ .'.format(d1))
print('Você Tem {:.2f}€ .'.format(e1))