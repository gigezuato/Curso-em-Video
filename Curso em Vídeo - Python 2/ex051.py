print('='*25)
print('10 TERMOS DE UMA PA')
print('='*25)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))

for i in range(1, 11):
    an = a1 + (i - 1) * r
    print(an, '-->', end=' ')
print('Acabou!')

'''outra forma:
    decimo = a1 + (decimo - 1) * r
    for c in range(a1, decimo, r):
        print('{}'.format(c), end=' -->')
    print('Acabou!')'''