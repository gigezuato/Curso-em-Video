frase = str(input('Digite uma frase:')).strip().lower()
frase = frase.replace('á', 'a')
frase = frase.replace('à', 'a')
frase = frase.replace('â','a')
frase = frase.replace('ã','a')
print('A letra A aparece {} vezes na frase.'.format(frase.count('a')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('a')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('a')+1))
