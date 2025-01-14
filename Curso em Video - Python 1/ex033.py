n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))
n3 = int(input('Terceiro valor:'))
# Verificando qual é menor
menor = n1
if n2 < n3 and n2 < n1:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Verificando qual é maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor valor digitado é {}'.format(menor))
print('O maior valor digitado é {}'.format(maior))

'''if n1 > n2 and n1 > n3:
    print('O maior valor digitado é {}'.format(n1)) #poderia criar uma variavel maior = n1
if n2 > n1 and n2 > n3:
    print('O maior valor digitado é {}'.format(n2))
if n3 > n1 and n3 > n2:
    print('O maior valor digitado é {}'.format(n3))

if n1 < n2 and n1 < n3:
    print('O menor valor digitado é {}'.format(n1))
if n2 < n1 and n2 < n3:
    print('O menor valor digitado é {}'.format(n2))
if n3 < n1 and n3 < n2:
    print('O menor valor digitado é {}'.format(n3))'''

