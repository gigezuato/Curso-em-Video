from colorama import Fore, Back, Style
from time import sleep


def pyhelp(funcionalidade):
    print(Fore.BLACK + Back.CYAN + '~' * 43)
    print(f"   Acessando o manual do comando '{funcionalidade}'")
    print('~' * 43)  # poderia ter criado uma função só para os títulos
    sleep(0.5)
    print(Style.RESET_ALL)
    print(Fore.BLACK + Back.LIGHTWHITE_EX)
    help(funcionalidade)
    print(Style.RESET_ALL)


while True:
    print(Fore.BLACK + Back.YELLOW + '~' * 30)
    print(f'   SISTEMA DE AJUDA PyHELP')
    print('~' * 30)
    print(Style.RESET_ALL)
    fun = str(input('Função ou Biblioteca > ')).lower().strip()
    if fun == 'fim':
        break
    else:
        pyhelp(fun)
        sleep(1)
print(Fore.BLACK + Back.LIGHTRED_EX + '~'*15)
print('   ATÉ LOGO!')
print('~'*15)
