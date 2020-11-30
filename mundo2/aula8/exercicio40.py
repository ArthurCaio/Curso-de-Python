no1 = float(input('Qual a nota da 1º unidade? '))
no2 = float(input('Qual a nota da 2º unidade? '))
no3 = float(input('Qual a nota da 3º unidade? '))
no4 = float(input('Qual a nota da 4º unidade? '))
media = (no1 + no2 + no3 + no4)/4
if media < 5.0:
    print('REPROVADO')
elif media >= 5.0 and media <= 6.9:
    print('RECUPERAÇÃO')
elif media >= 7.0:
    print('APROVADO')