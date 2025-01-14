num = int(input("Digite um número inteiro:"))
print("Escolha uma das bases para conversão:\n [ 1 ] converter para BINÁRIO\n [ 2 ] converter para OCTAL\n [ 3 ] "
      "converter para HEXADECIMAL\n ")
base = int(input("Sua escolha:"))

if base == 1:
    print('{} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
elif base == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Essa não é uma das opções!')
