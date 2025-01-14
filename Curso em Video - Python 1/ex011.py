la = float(input('Largura da parede:'))
h = float(input('Altura da parede:'))
area = la * h
t = area / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(la, h, area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(t))
