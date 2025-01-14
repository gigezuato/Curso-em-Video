from random import sample
a1 = input('Primeiro aluno:')
a2 = input('Segundo aluno:')
a3 = input('Terceiro aluno:')
a4 = input('Quarto aluno:')
lista = [a1, a2, a3, a4]
ordem = sample(lista, 4)

print('A ordem para a apresentação será {}'.format(ordem))

''' outro jeito: lista = [a1, a2, a3, a4]
    random.shuffle(lista)
    print(lista)'''
