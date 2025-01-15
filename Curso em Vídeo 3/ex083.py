abertos = []
fechados = []

exp = str(input('Digite uma expressão matemática: '))
for i, carac in enumerate(exp):
    if carac == '(':
        abertos.append(carac)
    elif carac == ')':
        fechados.append(carac)

if len(abertos) == len(fechados):
    print('Expressão correta!')
else:
    print('Expressão incorreta!')

# solucao do guanabara
'''
expr = str(input('Digite a expressão: ')
pilha = []
for simb in expr:    vai percorrer a expressao
    if simb == '(':
        pilha.append('(')    cada parentesis aberto ele adiciona na pilha
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()       se a pilha não estiver vazia, ele remove o ultimo item adicionado '('
        else:
            pilha.append(')')  senao, o parentesis ')' é adicionado na pilha
            break
if len(pilha) == 0:   se não houver mais itens na pilha, quer dizer que todos os parentesis fora fechados
    print('A expressão está correta!')
else:
    print('A expressão está incorreta!')
'''