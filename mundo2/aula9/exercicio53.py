frase = str(input('Digite algo: ')).replace(' ','').upper()
frasein = frase[::-1]
print('A palavra que você digitou é {}'.format(frase))
if frase == frasein:
    print('{} é um palíndromo'.format(frase))
else:
    print('{} não é um palíndromo'.format(frase))