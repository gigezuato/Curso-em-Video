print('-=' * 20)
print(f'{"Tabuadas": >20}')
print('-=' * 20)
while True:
    print('-' * 40)
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 40)
    if num < 0:
        break
    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')

print('Programa de Tabuadas encerrado! Até mais!')
