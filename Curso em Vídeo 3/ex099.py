from time import sleep


def maior(*nums):
    print('=-' * 20)
    print('Analizando os valores passados...')
    if nums == ():
        print('Foram informados 0 valores ao todo.')
        print('O maior valor informado foi 0.')
    else:
        for n in nums:
            print(n, end=' ', flush=True)
            sleep(0.5)
        print()
        print(f'Foram informados {len(nums)} valores ao todo.')
        print(f'O maior valor informado foi {max(nums)}.')
        '''poderia utilizar o método
            cont = maior = 0
            assim não iria precisar verificar se nenhum parâmetro foi passado
        '''


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
