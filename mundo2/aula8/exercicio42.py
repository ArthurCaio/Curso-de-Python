r1 = float(input('Digite O Valor da Primeira Reta: '))
r2 = float(input('Digite O Valor da Segunda Reta: '))
r3 = float(input('Digite O Valor da Terceira Reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    if r1 == r2 and r1 == r2 and r2 == r3:
        print('TRIANGULO EQUILATERO')
    elif r1 == r2 and r1 != 3 or r1 == r3 and r1 != r2 or r2 == r3 and r1 != r2:
        print('TRIANGULO ISOCELES')
    elif r1 != r2 and r1 != r3  and r2 != r3:
        print('TRIANGULO ESCALENO')
else:
    print('Não é Possivel Forma um Triangulo.')