import datetime
yb = int(input('Qual a ano que você nasceu? '))
cy = datetime.date.today().year
idade = cy - yb
if idade <= 9:
    print('Você é um Atleta Mirin.')
elif idade >= 10 and idade <= 14:
     print('Você é um Atleta Infantil.')
elif idade >= 15 and idade <= 19:
    print('Você é um Atleta Junior.')
elif idade == 20:
    print('Você é um Atleta Sênior')
elif idade > 20:
    print('Você é um Atleta Master')