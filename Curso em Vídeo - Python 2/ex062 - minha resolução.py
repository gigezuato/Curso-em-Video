print('Gerador de PA')
print('-=' * 10)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
a = a1
n = 1
termos = 10
cont = 10
while n <= 10:
    a = a1 + (n - 1) * r
    print(a, end=' -> ')
    n += 1
print('PAUSA')

i = 1
n = 11

while termos != 0:
    termos = int(input('Quantos termos você quer mostrar a mais? '))
    cont += termos
    while i <= termos:
        a = a1 + (n - 1) * r
        print(a, end=' -> ')
        n += 1
        i += 1
    print('PAUSA')
    i = 1
print(f'Progressão finalizada com {cont} termos mostrados.')



