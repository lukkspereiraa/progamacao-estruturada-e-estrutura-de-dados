lista_palavras = input('Digite uma lista de palavras separadas por espaço: ').split()

palavra_mais_longa = ''

for palavra in lista_palavras:
    if len(palavra) > len(palavra_mais_longa):
        palavra_mais_longa = palavra

print('A palavra mais longa é:', palavra_mais_longa)
