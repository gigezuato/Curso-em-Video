def aumentar(valor, taxa):
    resul = valor + (valor * (taxa / 100))
    round(resul, 2)
    return resul


def diminuir(valor, taxa):
    resul = valor - (valor * (taxa / 100))
    round(resul, 2)
    return resul


def metade(valor):
    resul = valor / 2
    round(resul, 2)
    return resul


def dobro(valor):
    resul = valor * 2
    round(resul, 2)
    return resul
