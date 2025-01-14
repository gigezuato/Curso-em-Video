import random
from random import randint
comp = random.randint(0, 10)
print('Eu sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
jog = 11
cont = 0

while jog != comp:
    cont = cont + 1
    jog = int(input('Qual é o seu palpite?'))
    if comp > jog:
        print('Mais... Tente mais uma vez!')
    elif comp < jog:
        print('Menos... Tente mais uma vez!')
    else:
        print('Acertou com {} tentativas. Parabéns!'.format(cont))


'''acertou = False
    palpites = 0
    while not acertou:
        jog = jog = int(input('Qual é o seu palpite?'))
        palpites += 1
        if jog == comp:
        acertou = True
        else:
            if jog < comp:
                print('Mais... Tente mais uma vez!')
            elif jog > comp:
                print('Menos... Tente mais uma vez!')
    print('Acertou com {} tentativas. Parabéns!'.format(palpites))'''
