c = float(input('Digite um a Temperatura Celsius : '))
f = c * 1.8 + 32.00
k = (f - 32)/1.8 + 273.15
r = c * 1.8 + 491.67
print('Fahrenheit : {}F°\nKelvin : {:.2f}K°\nRankine : {:.2f}R°'.format(f,k,r))