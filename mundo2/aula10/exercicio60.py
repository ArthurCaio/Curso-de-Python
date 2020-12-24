num: int = int(input('Digite um numero: '))
c = num
fat = 1
while c != 0:
    fat *= c
    c -= 1
print('A fatoração de {} é iqual a {}'.format(num,fat))