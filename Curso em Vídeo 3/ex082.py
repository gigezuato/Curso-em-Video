lista = []
pares = []
impares = []

while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break

for i in range(len(lista)):
    if lista[i] % 2 == 0:
        pares.append(lista[i])
    else:
        impares.append(lista[i])

print('-' * 40)
print(f'Os valores digitados foram: {lista}')
print(f'Os valores PARES digitados foram: {pares}')
print(f'Os valores IMPARES digitados foram: {impares}')
