def conta_letra(string, letra):
    """
    Conta quantas vezes uma determinada letra aparece em uma string.
    
    :param string: A string onde será feita a contagem.
    :param letra: A letra que será contada.
    :return: O número de vezes que a letra aparece na string.
    """
    contador = 0
    for char in string:
        if char == letra:
            contador += 1
    
    return contador

string = "desenvolvimento"
letra = "e"
print(conta_letra(string, letra))  # Saída esperada: 3
