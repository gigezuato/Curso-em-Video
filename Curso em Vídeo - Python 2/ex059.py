from time import sleep
n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))
opcao = 0
print('=-' * 20)
while opcao != 5:
    print(' [ 1 ] somar \n [ 2 ] multiplicar \n [ 3 ] maior \n [ 4 ] novos números \n [ 5 ] sair do programa')
    opcao = int(input('Qual é a sua opção?'))
    if opcao == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('A multiplicação de {} por {} é {}'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            print('Entre {} e {} o maior é o {}'.format(n1, n2, n1))
        elif n1 < n2:
            print('Entre {} e {} o maior é o {}'.format(n1, n2, n2))
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor:'))
        n2 = int(input('Segundo valor:'))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Tente novamente!')
    print('=-' * 20)
sleep(1)
print('=-' * 20)
print('Fim do programa! Volte sempre!')