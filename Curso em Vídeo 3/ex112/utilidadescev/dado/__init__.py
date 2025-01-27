def leia_dinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '' or entrada.isalnum():
            print(f'\033[0;31mErro: \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)



