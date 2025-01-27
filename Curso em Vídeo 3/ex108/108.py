from ex108 import moeda

preco = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {moeda.moeda(preco)} é R$ {moeda.moeda(moeda.metade(preco))}')
print(f'O dobro de R$ {moeda.moeda(preco)} é R$ {moeda.moeda(moeda.dobro(preco))}')
print(f'Aumentando 10%, temos R$ {moeda.moeda(moeda.aumentar(preco, 10))}')
print(f'Diminuindo 10%, temos R$ {moeda.moeda(moeda.diminuir(preco, 10))}')
