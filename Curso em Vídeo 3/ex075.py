nums = (int(input('Digite um número:')),
        int(input('Digite outro número:')),
        int(input('Digite mais um número:')),
        int(input('Digite o último número:')))
cont = 0
print(f'O valor 9 apareceu {nums.count(9)} vezes.')
if 3 in nums:
    print(f'O valor 3 aparece pela primeira vez na posição {nums.index(3) + 1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
for i in range(len(nums)):
    if nums[i] % 2 == 0:
        cont += 1
if cont > 0:
    print('Os valores pares foram: ', end='')
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            print(nums[i], end=' ')
else:
    print('Não foram digitados valores pares!')
