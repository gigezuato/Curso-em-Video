n = int(input('Digite o número para calcular o fatorial: '))
c = n
fat = 1
print(f'Calculando {n}! = ', end=' ')
while c > 0:
    print(f'{c}', end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    fat *= c
    c -= 1
print(fat)


'''n = int(input('Digite um número para calcular seu fatorial: '))
fat = 1

for i in range(n, 0, -1):
    if i == 1:
        print('1 = ', end=' ')
    else:
        print(f'{i} X ', end=' ')

while n > 0:
    fat *= n
    n -= 1
print(fat)'''

#from math import factorial
