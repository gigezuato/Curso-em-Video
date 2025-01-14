import random
import time
from random import choice
from time import sleep
print('Suas opções:')
print(' [ 0 ] PEDRA \n [ 1 ] PAPEL \n [ 2 ] TESOURA')
opcao = int(input('Qual a sua jogada?'))
itens = ('PEDRA', 'PAPEL', 'TESOURA')
comp = random.choice(itens)
print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO!!!')
time.sleep(0.5)
print('-=-'*10)
print('O computador jogou {}'.format(comp))
if opcao == 0:
    print('O jogador jogou PEDRA')
elif opcao == 1:
    print('O jogador jogou PAPEL')
elif opcao == 2:
    print('O jogador jogou TESOURA')
else:
    print('Essa é uma opção inválida, jogador!')
print('-=-'*10)

if comp == 'PEDRA' and opcao == 0 or comp == 'PAPEL' and opcao == 1 or comp == 'TESOURA' and opcao == 2:
    print('EMPATE!!!')
elif comp == 'PEDRA' and opcao == 2 or comp == 'PAPEL' and opcao == 0 or comp == 'TESOURA' and opcao == 1:
    print('COMPUTADOR VENCE!!!')
elif comp == 'PEDRA' and opcao == 1 or comp == 'PAPEL' and opcao == 2 or comp == 'TESOURA' and opcao == 0:
    print('JOGADOR VENCE!!!')
