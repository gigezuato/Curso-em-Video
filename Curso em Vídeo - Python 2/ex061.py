print('Gerador de PA')
print('-=' * 10)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
a = a1
n = 1
while n <= 10:
    a = a1 + (n - 1) * r
    print(a, end=' -> ')
    n += 1
print('FIM')


# a += r
