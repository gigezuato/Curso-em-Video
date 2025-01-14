s1 = float(input('Primeiro segmento:'))
s2 = float(input('Segundo segmento:'))
s3 = float(input('Terceiro segmento:'))
tri = bool(s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2)

if tri == True:
    if s1 == s2 == s3:
        print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO!')
    elif s1 == s2 or s1 == s3 or s2 == s3:
        print('Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES!')
    elif s1 != s2 != s3:
        print('Os segmentos acima PODEM FORMAR um triânglo ESCALENO!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo!')
