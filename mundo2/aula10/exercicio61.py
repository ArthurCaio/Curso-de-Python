print('============================')
print('   10 TERMOS  DE UM PA')
print('============================')
pt = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
c = 10
while c != 0:
    print('{} '.format(pt), end='')
    pt += r
    c -=1
print('FIM!')