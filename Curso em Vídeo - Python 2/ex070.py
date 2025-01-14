print('-' * 40)
print(f'{"MEGA LOJA" : >20}')
print('-' * 40)
total = mais_mil = cont = valor_barato = 0
produto_barato = ' '
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco

    if cont == 1:  # pode simplificar esse bloco colocando if cont == 1 or preco < valor_barato:
        valor_barato = preco
    else:
        if preco < valor_barato:
            valor_barato = preco
            produto_barato = nome

    if preco > 1000:
        mais_mil += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break

print('-' * 15, 'ESTATÍSTICAS', '-' * 15)  # print('{:-^40}'.format('ESTATÍSTICAS'))
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {mais_mil} produto(s) custando mais de R$ 1000.00')
print(f'O produto mais barato foi {produto_barato} que custa {valor_barato:.2f}')
