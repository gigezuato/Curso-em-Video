n = int(input('Digite um número: '))
div = 0

for i in range(1, n + 1):
    if n % i == 0:
        div += 1
        print('\033[33m', end=' ')
    else:
        print('\033[31m', end=' ')
    print('{}'.format(i), end=' ')
print('\n \033[mO número {} foi divisível {} vezes'.format(n, div))
if div == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
