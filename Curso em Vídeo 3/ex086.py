matriz = [[], [], []]

for i in range(3):
    for j in range(3):
        n = int(input(f'Digite o valor de [{i}, {j}]: '))
        matriz[i].append(n)
print('-=' * 20)
for i in range(3):
    for j in range(3):
        print(f'[ {matriz[i][j]:^5} ]', end='  ')
    print()
