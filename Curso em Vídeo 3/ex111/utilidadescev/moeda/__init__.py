def aumentar(valor=0, taxa=0, forma=False):
    resul = valor + (valor * (taxa / 100))
    return resul if forma is False else moeda(resul)


def diminuir(valor=0, taxa=0, forma=False):
    resul = valor - (valor * (taxa / 100))
    return resul if forma is False else moeda(resul)


def metade(valor=0, forma=False):
    resul = valor / 2
    return resul if forma is False else moeda(resul)


def dobro(valor=0, forma=False):
    resul = valor * 2
    return resul if forma is False else moeda(resul)


def moeda(valor=0.0, moeda='R$'):
    return f'{moeda}{valor:>8.2f}'.replace('.', ',')


def resumo(valor, aumento=10, desconto=5):
    print('-'*40)
    print('RESUMO DO VALOR'.center(40))
    print('-'*40)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{aumento}', '% de aumento:', f' \t{aumentar(valor, aumento, True)}')
    print(f'{desconto}', '% de desconto:', f' \t{diminuir(valor, desconto, True)}')
    print('-'*40)