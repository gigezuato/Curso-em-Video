from datetime import date
maior = 0
menor = 0
for i in range(1, 8):
    ano_nasc = int(input("Digite o ano de nascimento da {}º pessoa: ".format(i)))
    idade = date.today().year - ano_nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('Ao todo tivemos {} pessoas na maioridade.'.format(maior))
print('E também tivemos {} pessoas que não atingiram a maioridade.'.format(menor))

