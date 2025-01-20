def area(larg, comp):
    a = larg * comp
    return a   # poderia ter printado a resposta aqui ao invés de retornar


print('  Controle de Terrenos')
print('-'*30)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
print(f'A área de um terreno {largura} x {comprimento} é de {area(largura, comprimento):.2f} m²')
