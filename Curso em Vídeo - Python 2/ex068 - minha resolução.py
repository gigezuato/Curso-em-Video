from random import randint
print('-=' * 20)
print(f'{"JOGO DO PAR OU ÍMPAR": >30}')
print('-=' * 20)
soma = cont = 0
while True:
    jogador = int(input('Diga um valor: '))
    jog_escolha = ' '
    while jog_escolha not in 'PI':
        jog_escolha = str(input('Par ou Ímpar? [P/I]')).upper().strip()[0]
    print('-' * 40)
    computador = randint(0, 100)
    soma = jogador + computador
    if soma % 2 == 0 and jog_escolha == 'P':
        print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} deu PAR')
        print('-' * 40)
        print('Você VENCEU!')
        cont += 1
        print('Vamos jogar novamente...')
        print('-=' * 20)
    elif soma % 2 != 0 and jog_escolha == 'I':
        print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} deu ÍMPAR')
        print('-' * 40)
        print('Você VENCEU!')
        cont += 1
        print('Vamos jogar novamente...')
        print('-=' * 20)
    else:
        if soma % 2 == 0:
            print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} deu PAR')
            print('-' * 40)
            print('Você PERDEU!')
            print('-=' * 20)
            break
        else:
            print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} deu ÍMPAR')
            print('-' * 40)
            print('Você PERDEU!')
            print('-=' * 20)
            break

print(f'GAME OVER! Você venceu {cont} vezes.')
