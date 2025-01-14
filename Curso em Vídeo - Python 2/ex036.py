valor = float(input("Valor da casa: R$"))
sal = float(input("Salário do comprador: R$"))
anos = int(input("Quantos anos de financiamento?"))
meses = anos * 12
prest = valor / meses

print("Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}".format(valor, anos, prest))
if prest >= 0.30 * sal:
    print("Emprréstimo NEGADO!")
else:
    print("O empréstimo pode ser concedido!")

