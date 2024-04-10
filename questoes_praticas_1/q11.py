numeros = input('Digite uma lista de números separados por espaço: ').split()

numeros = [int(num) for num in numeros]
print('Números pares na lista:')

for num in numeros:
    if num % 2 == 0:
        print(num)
