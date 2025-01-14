nome = str(input('Digite seu nome completo:')).strip()
d = nome.split()
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras'.format(d[0], len(d[0])))

# print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))