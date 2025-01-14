palavras = ('aprender', 'programar', 'linguagem',
            'python', 'curso', 'gratis', 'estudar',
            'praticar', 'trabalhar', 'mercado',
            'programador', 'futuro')

for p in palavras:   # for p in palavras:
    print(f'Na palavra {p.upper()} temos ', end='')   # {palavras[p]}
    for letras in p:   # for letras in palavras[p]:
        if letras in 'aeiou':
            print(f'{letras.lower()}', end=' ')
    print('\n')

