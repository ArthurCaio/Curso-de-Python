import datetime  
ano = int(input('Digite qual Ano Você quer analisar?Digite 0 Para Analisar O ano que Você esta: '))
if ano == 0 :
    ano == datetime.date.today().year
if ano % 4 == 0 and 100 % ano != 0 or 400 % ano == 0:
    print('Esse Ano è Bissexto.')
else:
    print('Esse Ano não é Bissexto.') 