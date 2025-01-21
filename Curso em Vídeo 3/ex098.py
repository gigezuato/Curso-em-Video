from time import sleep


def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}')
    sleep(1.5)
    if passo < 0:
        fim -= 1
    elif passo > 0:
        fim += 1
    for n in range(inicio, fim, passo):  # poderia usar o while
        print(f'{n} ', end='', flush=True)
        sleep(0.5)
    print('FIM!')
    print('=-'*20)


contador(1, 10, 1)
contador(10, 0, -2)
print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
while p == 0:
    print('Erro! O passo não pode ser zero!')
    p = int(input('Passo: '))
print('=-'*20)
contador(i, f, p)
