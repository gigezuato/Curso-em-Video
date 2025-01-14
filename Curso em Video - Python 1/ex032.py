from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual:'))
if ano == 0:
    ano = date.today().year

if ano % 100 == 0:
    if ano % 400 == 0:
        print('O ano {} É bissexto.'.format(ano))
    else:
        print('O ano {} NÃO é bissexto.'.format(ano))
else:
    if ano % 4 == 0:
        print('O ano {} É bissexto.'.format(ano))
    else:
        print('O ano {} NÃO é bissexto.'.format(ano))

# ano = date. today(). year. Print = 2022.

'''if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print('O ano {} É bissexto.).format(ano)
    else:
        print('O ano {} NÃO é bissexto.).format(ano)'''
