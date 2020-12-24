num = int(input('escreva um numero: '))
print('escolha uma das alternativas abaixo')
print('1-Binario')
print('2-Octadecimal')
print('3-Hexadecimal')
con = int(input('Qual a sua opção: '))
if con == 1:
    print('{} convertido para BINARIO é igual a {}'.format(bin(num)[2:]))
elif con == 2:
    print('{} convertico para OCTAL é igual a {}'.format(num,oct(num)[2:]))
elif con == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('você não digitou um numero das alternativas.')
    print('>:(')