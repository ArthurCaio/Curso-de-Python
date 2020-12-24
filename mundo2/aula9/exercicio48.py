n = 0
for c in range (1,500,2):
    print(c)
    if c % 3 == 0:
        n += c
print('A soma de todos os numeros ímpares multiplos de 3 é igual a {}'.format(n))