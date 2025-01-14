leve = pesado = cont = 0
popul = []
pessoas = []
mais_pesado = []
mais_leve = []

while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    if cont == 0:
        leve = pessoas[1]
        pesado = pessoas[1]
    else:
        if pessoas[1] > pesado:
            pesado = pessoas[1]
        if pessoas[1] < leve:
            leve = pessoas[1]
    cont += 1
    popul.append(pessoas[:])
    pessoas.clear()
    resp = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break

for p in popul:
    if p[1] == pesado:
        mais_pesado.append(p[0])
    if p[1] == leve:
        mais_leve.append(p[0])
print('='*40)
print(f'O total de pessoas cadastradas foram: {len(popul)}')
print(f'O peso mais pesado foi {pesado} Kg de {mais_pesado}')
print(f'O peso mais leve foi {leve} Kg de {mais_leve}')