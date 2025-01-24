import moeda

preco = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {preco:.2f} é R$ {moeda.metade(preco)}')
print(f'O dobro de R$ {preco:.2f} é R$ {moeda.dobro(preco)}')
print(f'Aumentando 10%, temos R$ {moeda.aumentar(preco, 10)}')
print(f'Diminuindo 10%, temos R$ {moeda.diminuir(preco, 10)}')
