from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cadastros.txt'

if not arquivo_existe(arq):
    criar_arquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        # Opção Ver pessoas cadastradas
        ler_arquivo(arq)
    elif resposta == 2:
        # Opção Cadastrar nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: ').strip())
        idade = leia_int('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mErro! Digite uma opção válida!\033[m')
    sleep(2)



