print('=' * 40)
print(f"{'BANCO BG': >23}")
print('=' * 40)

cont_50 = cont_20 = cont_10 = cont_1 = 0
valor = int(input('Qual valor irá sacar? R$ '))
print('-' * 40)

while True:
    if valor >= 50:
        cont_50 = valor // 50
        valor = valor % 50
        print(f'Total de {cont_50} cédulas de R$ 50')
    elif valor >= 20:
        cont_20 = valor // 20
        valor = valor % 20
        print(f'Total de {cont_20} cédulas de R$ 20')
    elif valor >= 10:
        cont_10 = valor // 10
        valor = valor % 10
        print(f'Total de {cont_10} cédulas de R$ 10')
    else:
        if valor == 0:
            break
        else:
            cont_1 = valor
            print(f'Total de {cont_1} cédulas de R$ 1')
            break

print('=' * 40)
print('Volte sempre ao Banco BG! Tenha um ótimo dia!')
