numeros = input('Digite uma lista de números separados por espaço: ').split()

numeros = [int(num) for num in numeros]
print('Números menores que 5 :')

for num in numeros:
    if num < 5:
        print(num)
