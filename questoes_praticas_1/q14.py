numeros = input('Digite uma lista de números separados por espaço: ').split()

numeros = [int(num) for num in numeros]
print('Números maiores que 10 :')

for num in numeros:
    if num > 10:
        print(num)
