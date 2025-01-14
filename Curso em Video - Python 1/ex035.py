print('-='*25)
print('Analisador de Triângulos')
print('-='*25)
a = float(input('Primeiro segmento:'))
b = float(input('Segundo segmento:'))
c = float(input('Terceiro segmento:'))

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos NÃO PODEM FORMAR um triângulo!')
