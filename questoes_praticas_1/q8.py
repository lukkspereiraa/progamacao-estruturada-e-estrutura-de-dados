numeros = input('Digite uma lista de números separados por espaço :' ).split()

if numeros:
    maior_numero = max(map(float, numeros))
    print('O maior número da lista é:', maior_numero)
else:
    print('A lista está vazia.')
