numeros_str = input('Digite uma lista de números separados por espaço: ')
numeros_lista = numeros_str.split()
numeros_float = [float(numero) for numero in numeros_lista]

if numeros_float:
    media = sum(numeros_float) / len(numeros_float)
    print('A média dos números é:', media)
else:
    print('A lista está vazia.')
