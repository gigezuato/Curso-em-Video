from math import sqrt
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjascente:'))
hi = sqrt(co**2 + ca**2)
print('A hipotenusa vale {:.2f}'.format(hi))

''' from math import hypot 
    hi = math.hypot(co, ca)'''
