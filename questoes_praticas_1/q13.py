palavras = input('Digite uma lista de palavras separados por espaço: ').split()

palavras = [str(palavra) for palavra in palavras]
print('Todas as palavras que comecam com "A" ou "a" :')

for palavra in palavras:
    if palavra.lower().startswith('a'):
        print(palavra)
        