print('============================')
print('   10 TERMOS  DE UM PA')
print('============================')
pt = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
for c in range (0,10):
    print('{} '.format(pt),end='')
    pt += r
print('FIM!')