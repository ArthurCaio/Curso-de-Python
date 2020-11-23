vdc = float(input('Qual o valor da casa? '))
sala = float(input('Qual o seu salario? '))
qa = int(input('Digite em quantos anos vc deseja comprar a casa? '))
pres = vdc / qa
if pres >= (sala * 30) / 100:
    print('vc não pode compra essa casa')
else:
    print('vc pode comprar essa casa')
    print('Pagando {:.2f}R$ por mês'.format(pres))
