matriz = [[], [], []]
soma_pares = soma_terColuna = maior_segLinha = 0
for i in range(3):
    for j in range(3):
        n = int(input(f'Digite o valor de [{i}, {j}]: '))
        if n % 2 == 0:
            soma_pares += n
        if j == 2:
            soma_terColuna += n
        if i == 1:
            if j == 0 or n > maior_segLinha:
                maior_segLinha = n
        matriz[i].append(n)
print('-=' * 30)
for i in range(3):
    for j in range(3):
        print(f'[ {matriz[i][j]:^5} ]', end='  ')
    print()
print('-='*30)
print(f'A soma dos valores pares da matriz é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {soma_terColuna}')
print(f'O maior valor da segunda linha é {maior_segLinha}')