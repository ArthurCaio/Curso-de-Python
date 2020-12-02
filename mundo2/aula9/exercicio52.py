num = int(input('Digite um numero: '))
d = 0
for c in range (1,num+1):
    if num % c == 0:
        print('\033[0;33m', end='')
        d += 1
    else:
        print('\033[0;31m', end='')
    print('{} '.format(c), end='')
print('')
print('\033[m{} é pode ser dividido {} vezes'.format(c,d))
if d >= 3:
    print('{} Não é um número Primo.'.format(c))
else:
    print('{} é um número Primo.'.format(c))