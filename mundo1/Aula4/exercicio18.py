import math
n = float(input('Digite um Valor: '))
cos = math.cos(math.radians(n))
sin = math.sin(math.radians(n))
tan = math.tan(math.radians(n))
print('O Coseno de {} é {:.2f} \nO Seno de {} é {:.2f} \nO Tangente de {} é {:.2f}'.format(n,cos,n,sin,n,tan))