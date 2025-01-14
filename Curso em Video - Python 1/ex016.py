from math import trunc
x = float(input('Digite um valor:'))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(x, trunc(x)))
# ou usa o int() nesse caso não precisa importar