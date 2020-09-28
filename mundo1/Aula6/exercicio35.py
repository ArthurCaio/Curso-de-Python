r1 = float(input('Digite O Valor da Primeira Reta: '))
r2 = float(input('Digite O Valor da Segunda Reta: '))
r3 = float(input('Digite O Valor da Terceira Reta: '))
if r1< r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print("É Possivel Forma um Triangulo.")
else:
    print('Não é Possivel Forma um Triangulo.')