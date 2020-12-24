import datetime
y = int(input('Em que ano você nasceu ? '))
cy = datetime.date.today().year
idade = cy - y
if idade <= 17:
    print('Ainda falta {} anos para você si alistar'.format(18 - idade))
elif idade == 18:
    print('Você já pode si alistar,vá o mais rapido possivel.')
elif idade >= 19:
    r = str(input('Você ja si alistou?[S/n]'))
    if r == 'S' or r == 's':
        print('Obrigado por servir ao nosso pais :).')
    else:
        print('Você si atrasou {} anos para o alistamento :( .'.format(idade - 18))