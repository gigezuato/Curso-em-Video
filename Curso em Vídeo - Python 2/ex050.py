soma = 0
cont = 0
for i in range(1, 7):
    n = int(input('Digite o {} número:'.format(i)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Você informou {} números PARES e a soma deles é {}'.format(cont, soma))
