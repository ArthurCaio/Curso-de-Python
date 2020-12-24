a = int(input('Digite Um Numero: '))
b = int(input('Digite Outro Numero: '))
c = int(input('Digite Outro Numero: '))
menor = a
maior = c
if b<a and b<c :
    menor = b
if c<b and c<a:
    menor = c
if a>b and a>c:
    maior = a
if b>a and b>c:
    maior = b
print('O Menor numero é {}'.format(menor))
print('O Maior numero é {}'.format(maior))