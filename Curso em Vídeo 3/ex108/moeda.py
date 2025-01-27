def aumentar(valor=0, taxa=0):
    resul = valor + (valor * (taxa / 100))
    round(resul, 2)
    return resul


def diminuir(valor=0, taxa=0):
    resul = valor - (valor * (taxa / 100))
    round(resul, 2)
    return resul


def metade(valor=0):
    resul = valor / 2
    round(resul, 2)
    return resul


def dobro(valor=0):
    resul = valor * 2
    round(resul, 2)
    return resul


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:>8.2f}'.replace('.', ',')

