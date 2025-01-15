from datetime import datetime

ano_atual = datetime.now().year
dados = dict()
dados['Nome'] = str(input('Nome: '))
ano_nasc = int(input('Ano de nascimento: '))
dados['Idade'] = ano_atual - ano_nasc
dados['CTPS'] = int(input('Carteira de trabalho(0 se não tiver): '))
if dados['CTPS'] != 0:
    dados['Ano de contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: '))
    dados['Idade de aposentadoria'] = dados['Idade'] + ((dados['Ano de contratação'] + 35) - ano_atual)

print('='*30)
for k, v in dados.items():
    print(f'{k} é {v}')