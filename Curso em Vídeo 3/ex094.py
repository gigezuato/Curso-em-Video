cadastros = []
pessoas = {}
soma = 0
while True:
    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
    while pessoas['sexo'] not in 'FM':  # poderia usar while True
        print('Por favor, digite apenas M ou F.')
        pessoas['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
    pessoas['idade'] = int(input('Idade: '))
    cadastros.append(pessoas.copy())
    pessoas.clear()  # dá certo colocá-lo aqui, mas também la no começo após o while True
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while resp not in 'NS':  # tambpem poderia ser while True
        print('ERRO! Responda apenas S ou N.')
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
for i in range(len(cadastros)):
    soma += cadastros[i]['idade']
media = soma / len(cadastros)
print('-='*40)
print(f'A)  Ao todo temos {len(cadastros)} pessoas cadastradas.')
print(f'B)  A média de idades é de {media:.2f} anos.')
print('C)  As mulheres cadastradas foram ', end='')
for c in range(len(cadastros)):  # poderia fazer for c in cadastros (mais simples)
    if cadastros[c]['sexo'] == 'F':  # if c['sexo'] == 'F'
        print(f'{cadastros[c]['nome']}', end=' ')
print()
print('D)  Lista de pessoas que estão acima da média de idades: ')
for c in range(len(cadastros)):
    if cadastros[c]['idade'] > media:  # mesma coisa que ali em cima
        print(f'{'nome':>10} = {cadastros[c]['nome']}; sexo = {cadastros[c]['sexo']}; idade = '
              f'{cadastros[c]['idade']};')  # poderia ter usado for k, v in pessoas.items():
print('ENCERRADO!')