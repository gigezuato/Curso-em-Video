from random import randint
from time import sleep
from operator import itemgetter

jogo = {
    'Jogador 1': randint(1, 6),
    'Jogador 2': randint(1, 6),
    'Jogador 3': randint(1, 6),
    'Jogador 4': randint(1, 6)
}
print('Valores sorteados: ')
ranking = []
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('='*3, f'{'RANKING DOS JOGADORES':^3}', '='*3)
for i, n in enumerate(ranking):
    print(f'{i+1}º lugar: {n[0]} com {n[1]}')
    sleep(1)