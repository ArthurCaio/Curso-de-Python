s = float(input('Digite o seu Salario: '))
if s <= 1250:
    s = s + (s*15)/100
    print('O seu novo salario será de R${:.2f}'.format(s))
else:
    s = s + (s*10)/100 
    print('O seu novo salario será de R${:.2f}'.format(s))
print('Fim Programa...')