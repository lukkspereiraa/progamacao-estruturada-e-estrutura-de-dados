soma = 0

numeros = input('Digite uma lista de números separados por espaço: ').split()

numeros = [int(num) for num in numeros]

for num in numeros:
    if num % 2 != 0:
        soma = soma + num

print(soma, ' essa é a soma de todos os numeros impares')