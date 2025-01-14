from math import cos, sin, tan, radians
ang = float(input('Digite o ângulo que você deseja:'))
sen = sin(radians(ang))
cos = cos(radians(ang))
tg = tan(radians(ang))

print('O ângulo de {:.1f}° tem o SENO de {:.2f}'.format(ang, sen))
print('O ângulo de {:.1f}° tem o COSSENO de {:.2f}'.format(ang, cos))
print('O ângulo de {:.1f}° tem a TANGENTE de {:.2f}'.format(ang, tg))


