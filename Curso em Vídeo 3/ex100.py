from random import sample
from time import sleep


def sorteia():
    lista = (sample(range(11), 5))
    print('Foram sorteados os números: ')
    for c in lista:
        print(c, end=' ')
        sleep(0.4)
    print('PRONTO!')
    return lista


def soma_par(nums):
    soma = 0
    for i in nums:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {nums} temos {soma}')


n = sorteia()
soma_par(n)
