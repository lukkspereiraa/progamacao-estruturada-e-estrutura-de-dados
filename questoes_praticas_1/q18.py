produto = 1

numeros = input('Digite uma lista de números separados por espaço: ').split()

numeros = [int(num) for num in numeros]

for num in numeros:
        produto = produto * num

print(produto, ' essa é o produto de todos os numeros ')
