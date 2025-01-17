dados = list()
jogador = dict()
while True:
    total = 0
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input('Quantas partidas ele jogou? '))
    jogador['gols'] = list()
    for i in range(partidas):
        gols = int(input(f'Quantos gols na partida {i+1}? '))
        jogador['gols'].append(gols)
        total += gols
    jogador['total'] = total
    dados.append(jogador.copy())
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break

print('-='*40)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(dados):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)

while True:
    cod = int(input('Mostrar dados de qual jogador? [999 para parar]: '))
    if cod == 999:
        break
    elif cod not in range(len(dados)):
        print(f'ERRO! Não existe jogador com o código {cod}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {dados[cod]['nome']}:')
        for c, g in enumerate(dados[cod]['gols']):
            print(f'{'No jogo ': >6}{c+1} fez {g} gols.')
    print('-'*40)
print('<< VOLTE SEMPRE >>')