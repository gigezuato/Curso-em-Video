dados = {}
dados['Nome'] = str(input('Nome do Jogador: '))
dados['Gols'] = []   # poderia ter criado uma variável gols = list() e ir dando append nela
partidas = int(input(f'Quantas partidas {dados['Nome']} jogou? '))
for i in range(partidas):
    gols = int(input(f'Quantos gols na partida {i}? '))
    dados['Gols'].append(gols)  # aqui era só fazer dados['Gols'] = gols[:]
dados['Total de gols'] = sum(dados['Gols'])
print('-='*50)
print(dados)
print('-='*50)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*40)
print(f'O jogador {dados['Nome']} jogou {len(dados['Gols'])} partidas.')
for i in range(partidas):  # poderia ter feito for i, v in enumerate(dados['Gols']):
    print(f'{'=>':>5} Na partida {i}, fez {dados['Gols'][i]} gols.')
print(f'Foi um total de {dados['Total de gols']} gols.')
