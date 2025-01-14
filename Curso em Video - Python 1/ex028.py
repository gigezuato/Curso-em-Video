from random import randint
from time import sleep
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
sorteio = randint(0, 5)
n = int(input('Em que número eu pensei?'))
print('PROCESSANDO...')
sleep(2)
if n == sorteio:
    print('PARABÉNS, você acertou! Pensei no número {}'.format(sorteio))
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(sorteio, n))
#poderia usar o random.choice() também
