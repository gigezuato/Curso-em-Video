print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
n1 = 0
n2 = 1
soma = 0
termos = int(input('Quantos termos você quer mostrar? '))
print('~'*30)
print(n1, n2, sep=' -> ', end=' -> ')

for i in range(termos - 2):
    soma = n1 + n2
    print(soma, end=' ')
    print(' -> ' if i < (termos - 2) - 1 else ' -> FIM ', end=' ')
    n1 = n2
    n2 = soma

# com o while =>
'''n = int(input('Quantos termos você quer mostrar?'))
t1 = 0
t2 = 1
print(t1, t2, end=' ')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(t3, end=' ')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')
'''
