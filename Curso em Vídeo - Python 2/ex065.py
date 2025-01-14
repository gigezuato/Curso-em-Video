resp = 's'
cont = soma = maior = menor = 0
while resp != 'N':    # poderia ser while resp in 'sS':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num < menor:
            menor = num
        if num > maior:
            maior = num
    resp = input('Quer continuar? [S/N] ').upper().strip()[0]   # o 0 considera só a primeira letra

media = soma / cont
print(f'Você digitou {cont} números e a média foi {round(media, 2)}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
