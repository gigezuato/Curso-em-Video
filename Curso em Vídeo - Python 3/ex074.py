from random import sample
sorteio = (sample(range(1, 11), 5))
print('Os valores sorteados foram: ', end='')
for n in sorteio:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi {max(sorteio)}')
print(f'O menor valor sorteado foi {min(sorteio)}')
