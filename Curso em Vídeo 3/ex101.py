def voto(ano):
    from datetime import datetime
    ano_atual = datetime.now().year
    idade = ano_atual - ano
    print(f'Com {idade}: ', end='')
    if idade < 16:
        print('voto NEGADO!')
    elif 16 <= idade < 18 or idade >= 70:
        print('voto é OPCIONAL!')
    else:
        print('voto OBRIGATÓRIO!')


print('-'*30)
nasc = int(input('Qual o ano de nascimento? '))
voto(nasc)