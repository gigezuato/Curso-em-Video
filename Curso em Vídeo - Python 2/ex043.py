peso = float(input('Digite seu peso em kg:'))
altura = float(input('Digite sua altura em metros:'))
imc = peso / (altura ** 2)

print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal!')
elif 18.5 <= imc < 25:
    print('Parabéns! Você está na faixa de PESO NORMAL!')
elif 25 <= imc < 30:
    print('Você está na faixa de SOBREPESO!')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE!')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
