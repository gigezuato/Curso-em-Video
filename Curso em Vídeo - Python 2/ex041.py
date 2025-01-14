from datetime import date
anoNasc = int(input('Ano de nascimento:'))
idade = date.today().year - anoNasc
print('O atleta tem {} anos'.format(idade))

if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14: # idade < 9 and idade <= 14
    print('Classificação: INFANTIL')
elif idade <= 19: # idade < 14 and idade <= 19
    print('Classificação: JUNIOR')
elif idade <= 25: # idade < 19 and idade <= 25
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')

