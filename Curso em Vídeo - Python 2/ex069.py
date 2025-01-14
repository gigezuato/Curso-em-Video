deMaior = homens = mulheres_menos20 = 0
while True:
    print('-' * 40)
    print(f'{"CADASTRO" : >20}')
    print('-' * 40)

    idade = int(input('Idade: '))
    while idade < 0:
            idade = int(input('Digite uma idade válida: '))

    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    while sexo not in 'FM':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]

    if idade >= 18:
        deMaior += 1
    if sexo == 'M':
        homens += 1
    if idade < 20 and sexo == 'F':
        mulheres_menos20 += 1
        
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break


print(f'Total de pessoas com mais de 18 anos => {deMaior}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'Foram cadastradas {mulheres_menos20} mulheres com menos de 20 anos.')
