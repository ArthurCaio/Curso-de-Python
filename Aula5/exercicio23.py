n = int(input('Digite um Numero: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
um = n // 1000 % 10
print('unidade : {} \nDezena : {} \nCentena : {} \nUnidade de Milhar : {}'.format(u,d,c,um))