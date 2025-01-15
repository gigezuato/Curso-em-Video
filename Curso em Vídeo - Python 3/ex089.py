from time import sleep

alunos_geral = []
aluno = []
media = 0
'''poderia ter calculado a média dentro desse primeiro loop, após pedir as notas, 
e adicioná-la na lista alunos_geral'''
print('='*30)
while True:
    nome = str(input('Nome: '))
    aluno.append(nome)
    nota1 = float(input('Nota 1: '))
    aluno.append(nota1)
    nota2 = float(input('Nota 2: '))
    aluno.append(nota2)
    alunos_geral.append(aluno[:])
    aluno.clear()
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('='*30)
print(f'{'índices':^10}', f'{'nomes':^10}', f'{'médias':^10}')
print('-'*30)
for i, dados in enumerate(alunos_geral):
    media = (dados[1] + dados[2]) / 2
    print(f'{i:^10}', f'{dados[0]:^10}', f'{media:^10.1f}')

print('-'*30)
while True:
    op = int(input('Mostrar notas de qual aluno? [999 interrompe] '))
    if op == 999:
        break
    if op <= len(alunos_geral) - 1:
        for i, dados in enumerate(alunos_geral):
            if op == i:
                print(f'Notas de {dados[0]} são [{dados[1]}, {dados[2]}]')
print('-'*30)
print('FINALIZANDO...')
sleep(1)
print('PROGRAMA ENCERRADO!')