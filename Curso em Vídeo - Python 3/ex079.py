nums = []
while True:
    n = int(input('Digite um valor: '))
    if n in nums:
        print('Valor duplicado! Não vou adicionar...')
    else:
        nums.append(n)
        print('Valor adicionado!')

    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break

print('-=' * 40)
nums.sort()
print(f'Os números digitados foram: {nums}')
