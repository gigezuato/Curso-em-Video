nums = [[], []]

for i in range(7):
    n = int(input(f'Digite o {i+1}° valor: '))
    if n % 2 == 0:
        nums[0].append(n)
    else:
        nums[1].append(n)

nums[0].sort()
nums[1].sort()
print(f'Os valores pares são: {nums[0]}')
print(f'Os valores ímpares são: {nums[1]}')