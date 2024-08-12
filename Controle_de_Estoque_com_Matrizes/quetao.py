estoque = [ 
    [120, 80, 30, 45, 60],
    [70, 55, 90, 120, 30], 
    [110, 75, 60, 85, 100], 
    [80, 95, 55, 65, 70] 
]

def consultar_estoque(armazem, produto):
    """
    Permite consultar a quantidade de um produto em um armazém específico.
    :param armazem: Índice do armazém (0 a 3).
    :param produto: Índice do produto (0 a 4).
    :return: Quantidade do produto no armazém.
    """
    if 0 <= armazem < len(estoque) and 0 <= produto < len(estoque[0]):
        return estoque[armazem][produto]
    else:
        return "Armazém ou produto inválido."

def transferir_produto(armazem_origem, armazem_destino, produto, quantidade):
    """
    Transfere uma quantidade específica de um produto de um armazém para outro.
    :param armazem_origem: Índice do armazém de origem (0 a 3).
    :param armazem_destino: Índice do armazém de destino (0 a 3).
    :param produto: Índice do produto (0 a 4).
    :param quantidade: Quantidade a ser transferida.
    """
    if (0 <= armazem_origem < len(estoque) and 
        0 <= armazem_destino < len(estoque) and 
        0 <= produto < len(estoque[0]) and 
        quantidade > 0 and 
        estoque[armazem_origem][produto] >= quantidade):
        
        estoque[armazem_origem][produto] -= quantidade
        estoque[armazem_destino][produto] += quantidade
        return "Transferência realizada com sucesso."
    else:
        return "Erro na transferência. Verifique os parâmetros."

def total_produtos():
    """
    Calcula a quantidade total de cada produto disponível em todos os armazéns.
    :return: Lista com a quantidade total de cada produto.
    """
    total = [0] * len(estoque[0])
    for i in range(len(estoque[0])):
        total[i] = sum(estoque[j][i] for j in range(len(estoque)))
    return total

def armazem_maior_quantidade(produto):
    """
    Identifica qual armazém possui a maior quantidade de um determinado produto.
    :param produto: Índice do produto (0 a 4).
    :return: Índice do armazém com a maior quantidade do produto.
    """
    if 0 <= produto < len(estoque[0]):
        armazem_max = max(range(len(estoque)), key=lambda x: estoque[x][produto])
        return armazem_max
    else:
        return "Produto inválido."

def produtos_abaixo_critico(critico=50):
    """
    Identifica os produtos que têm estoque abaixo de um valor crítico em qualquer armazém.
    :param critico: Valor crítico para o estoque.
    :return: Lista de tuplas (produto, armazém) onde o estoque é abaixo do crítico.
    """
    abaixo_critico = []
    for produto in range(len(estoque[0])):
        for armazem in range(len(estoque)):
            if estoque[armazem][produto] < critico:
                abaixo_critico.append((produto, armazem))
    return abaixo_critico

def relatorio_estoque():
    """
    Gera um relatório com a soma total de todos os produtos em cada armazém e identifica
    o armazém com maior e menor quantidade de estoque total.
    :return: Tuplas contendo o armazém com maior e menor quantidade total de estoque.
    """
    totais_armazem = [sum(estoque[i]) for i in range(len(estoque))]
    max_estoque = max(totais_armazem)
    min_estoque = min(totais_armazem)
    armazem_max = totais_armazem.index(max_estoque)
    armazem_min = totais_armazem.index(min_estoque)
    
    return totais_armazem, armazem_max, armazem_min


print(f"Quantidade do produto 2 no armazém 1: {consultar_estoque(1, 2)}")

print(transferir_produto(0, 2, 3, 10))

print("Quantidade total de cada produto:", total_produtos())

print(f"Armazém com a maior quantidade do produto 1: {armazem_maior_quantidade(1)}")

print("Produtos com estoque abaixo de 50 unidades:", produtos_abaixo_critico(50))

totais_armazem, armazem_max, armazem_min = relatorio_estoque()
print("Soma total de todos os produtos em cada armazém:", totais_armazem)
print(f"Armazém com maior estoque total: {armazem_max}, Armazém com menor estoque total: {armazem_min}")
