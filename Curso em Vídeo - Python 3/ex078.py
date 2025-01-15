nums = []

for pos in range(0, 5):
    n = int(input(f'Digite um número para a posição {pos}: '))
    nums.append(n)  # poderia colocar direto: nums.append(int(input(f'Digite um número para a posição {pos}: ')))

print('-='*40)
print(f'Você digitou os números: {nums}')
print(f'O maior valor digitado foi {max(nums)} nas posições ', end='')
for p, num in enumerate(nums):
    if num == max(nums):
        print(f'{p}... ', end='')
print()
print(f'O menor valor digitado foi {min(nums)} nas posições ', end='')
for p, num in enumerate(nums):
    if num == min(nums):
        print(f'{p}... ', end='')
print()

# ao invés de usar as funções max e min, poderia fazer declarando variáveis maior e menor, igualando elas no primeiro
# loop e ir comparando depois