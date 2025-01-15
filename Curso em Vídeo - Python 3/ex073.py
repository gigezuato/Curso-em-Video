times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Internacional', 'Fortaleza', 'São Paulo', 'Bahia', 'Corinthians',
         'Cruzeiro', 'EC Vitória BA', 'Grêmio', 'Vasco Gama', 'Atlético Mineiro', 'CA Paranaense', 'EC Juventude',
         'Fluminense', 'Criciúma', 'Red Bull Bragantino', 'Cuiabá Esporte Clube', 'AC Goianiense')
print('=' * 40)
print(f'Lista de times do Brasileirão 2024: {times}')
print('-=' * 20)
print(f'Os 5 primeiros são: {times[:5]}')
print('-=' * 20)
print(f'Os 4 últimos são: {times[16:]}')  # ou: times[-4:]
print('-=' * 20)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 20)
print(f'O Corinthians está na {times.index("Corinthians") + 1} posição.')
print('=' * 40)
