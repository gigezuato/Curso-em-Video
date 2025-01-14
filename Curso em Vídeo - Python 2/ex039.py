from datetime import date
anoAtual = date.today().year
genero = str(input('Coloque M se for mulher e H se for homem:')).upper().strip()[0]
anoNasc = int(input('Ano de nascimento:'))
idade = anoAtual - anoNasc

if genero == 'H':
    print('Quem nasceu em {} tem {} anos em {}.'.format(anoNasc, idade, anoAtual))
    if idade < 18:
        saldo = 18 - idade
        print('Ainda faltam {} anos para o alistamento'.format(saldo))
        print('Seu alistamento será em {}'.format(anoAtual + saldo))
    elif idade > 18:
        saldo = idade - 18
        print('Você já deveria ter se alistado há {} anos'.format(saldo))
        print('Seu alistamento foi em {}'.format(anoAtual - saldo))
    else:
        print('Você tem que se alistar IMEDIATAMENTE!')
elif genero == 'M':
    print('O alistamento não é obrigatório para mulheres!')
else:
    print('Essa não é uma opção!')
