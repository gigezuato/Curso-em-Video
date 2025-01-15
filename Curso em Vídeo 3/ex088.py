from time import sleep
from random import sample

print('-'*30)
print(f'{'JOGA NA MEGA SENA':^30}')
print('-'*30)
mega = []
quant = int(input('Quantos jogos você quer gerar? '))
print('-='*3, f'SORTEANDO {quant} JOGOS', '-='*3)
for i in range(quant):
    jogo = list(sample(range(1, 61), 6))
    jogo.sort()
    mega.append(jogo[:])
    print(f'Jogo {i+1}: {jogo}')
    jogo.clear()
    sleep(1)
print('-='*5, '< BOA SORTE! >', '-='*5)