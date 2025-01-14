soma = cont = num = 0
# outra forma é ler o num aqui
while num != 999:
    #colocar soma e cont primeiro
    num = int(input('Digite um número [999 para parar]: ')) # e ler o num novamente por último
    if num != 999:
        soma += num
        cont += 1
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')

