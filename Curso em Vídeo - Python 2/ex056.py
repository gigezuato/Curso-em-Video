velho = 0
nome_velho = ' '
cont_menores = 0
soma_idades = 0
for p in range(1, 5):
    print('-'*10, '{} pessoa'.format(p), 10*'-')
    nome = str(input('Digite o nome da {} pessoa: '.format(p)))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()
    soma_idades += idade
    if p == 1:
        velho = idade
        nome_velho = nome
    else:
        if sexo == 'M':
            if idade > velho:
                nome_velho = nome
        elif sexo == 'F':
            if idade < 20:
                cont_menores += 1

media = soma_idades / 4
print('A média de idades do grupo é {}'.format(media))
print('O homem mais velho do grupo é {}'.format(nome_velho))
print('A quantidade de mulheres menores de 20 anos é {}'.format(cont_menores))
