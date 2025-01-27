from ex109 import moeda

preco = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {moeda.moeda(preco)} é R$ {moeda.metade(preco, True)}')
print(f'O dobro de R$ {moeda.moeda(preco)} é R$ {moeda.dobro(preco, True)}')
print(f'Aumentando 10%, temos R$ {moeda.aumentar(preco, 10, True)}')
print(f'Diminuindo 10%, temos R$ {moeda.diminuir(preco, 10, True)}')
