from colorama import Fore


def leia_int(msg):
    # outra forma seria colocar uma variável ok = False
    while True:
        num = input(msg)
        if num.isnumeric():
            numero = int(num)  # ok = True
            break
        else:
            print(Fore.RED + 'ERRO! Digite um número inteiro válido.', Fore.RESET)
        '''
        if ok:
            break
        '''
    return numero


n = leia_int('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
