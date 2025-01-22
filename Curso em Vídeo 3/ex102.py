def fatorial(n, show=False):
    """
        -> Calcula o fatorial de um número.
    :param n: Número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    fat = 1
    for cont in range(n, 0, -1):
        fat *= cont
        if show:
            print(f'{cont}', end=' ')
            print('=' if cont == 1 else 'X', end=' ')
    print(fat)


num = int(input('Digite o número: '))
print('-'*30)
fatorial(num, show=True)