soma = 0

numero_de_repeticoes = int(input('Digite quantos numeros você quer somar '))

for i in range(numero_de_repeticoes, 0, -1):
    nuemro = int(input('Digite um numero '))
    soma = soma + nuemro

print('A soma de todos os numeros é {}'.format(soma))