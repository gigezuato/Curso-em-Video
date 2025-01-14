print('{:=^40}'.format(" LOJAS GEZUATO "))
valor = float(input('Preço das compras: R$'))
print('Formas de PAGAMENTO')
print(' [ 1 ] à vista dinheiro/cheque \n [ 2 ] à vista cartão \n [ 3 ] 2x no cartão \n [ 4 ] 3x ou mais no cartão')
forma = int(input('Qual é a opção?'))

if forma == 1:
    total = valor * 0.90
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(valor, total))
elif forma == 2:
    total = valor * 0.95
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(valor, total))
elif forma == 3:
    valorPar = valor / 2
    print('A compra de R$ {:.2f} terá duas parcelas de R$ {:.2f}'.format(valor, valorPar))
elif forma == 4:
    parcelas = int(input('Qunatas parcelas?'))
    total = valor * 1.20
    valorPar = total / parcelas
    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS, sendo as parcelas de R$ {:.2f}'.format(parcelas, total, valorPar))
else:
    print('Essa não é uma opção válida!')
