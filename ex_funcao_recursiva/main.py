def resolver_labirinto(labirinto, pos_atual, pos_saida, visitados=None):
    if visitados is None:
        visitados = set()

    if pos_atual == pos_saida:
        return True

    linha_atual, coluna_atual = pos_atual

    if (linha_atual < 0 or linha_atual >= len(labirinto) or
            coluna_atual < 0 or coluna_atual >= len(labirinto[0]) or
            labirinto[linha_atual][coluna_atual] == 1 or
            pos_atual in visitados):
        return False

    visitados.add(pos_atual)

    if (resolver_labirinto(labirinto, (linha_atual - 1, coluna_atual), pos_saida, visitados) or  # cima
            resolver_labirinto(labirinto, (linha_atual + 1, coluna_atual), pos_saida, visitados) or  # baixo
            resolver_labirinto(labirinto, (linha_atual, coluna_atual - 1), pos_saida, visitados) or  # esquerda
            resolver_labirinto(labirinto, (linha_atual, coluna_atual + 1), pos_saida, visitados)):  # direita
        return True

    visitados.remove(pos_atual)
    return False

labirinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

entrada = (0, 0)  
saida = (4, 4)    

resultado = resolver_labirinto(labirinto, entrada, saida)
print("Caminho encontrado:", resultado)

