print('-'*40)
print(f'{'LISTAGEM DE PREÇOS': >27}')
print('-'*40)

produto_preco = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
                 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
                 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
for i, obj_pre in enumerate(produto_preco):
    if produto_preco.index(obj_pre) % 2 == 0:
        print(f'{produto_preco[i]:.<12}', end='')
    else:
        print(f'{'R$':.>19}', end='')
        print(f'{produto_preco[i]:>8}')

print('-'*40)
