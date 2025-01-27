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

