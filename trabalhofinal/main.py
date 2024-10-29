# Classe que representa um nó da árvore AVL
class Node:
    def __init__(self, chave, valor):
        """
        Inicializa um nó da árvore AVL.

        Parâmetros:
        - chave (qualquer tipo comparável): Chave pela qual o nó será ordenado (ex: nome do produto).
        - valor (qualquer tipo): O valor associado ao nó (ex: o produto em si).
        
        Atributos:
        - chave: Guarda a chave de ordenação.
        - valor: O valor que será armazenado junto com o nó.
        - altura: A altura do nó, utilizada para manter o balanceamento da árvore.
        - esquerda: Aponta para o nó filho à esquerda (inicialmente None).
        - direita: Aponta para o nó filho à direita (inicialmente None).
        """
        self.chave = chave  
        self.valor = valor  
        self.altura = 1  
        self.esquerda = None  
        self.direita = None  


# Classe que implementa a árvore AVL
class AVLTree:
    def __init__(self):
        """
        Inicializa uma árvore AVL vazia.
        
        Atributos:
        - raiz: O nó raiz da árvore (inicialmente None).
        """
        self.raiz = None

    def obter_altura(self, node):
        """
        Obtém a altura de um nó na árvore.

        Parâmetros:
        - node (Node): O nó para o qual queremos obter a altura.

        Retorno:
        - int: A altura do nó. Retorna 0 se o nó for None.
        """
        if not node:
            return 0
        return node.altura

    def obter_fator_balanceamento(self, node):
        """
        Calcula o fator de balanceamento de um nó.

        Parâmetros:
        - node (Node): O nó para o qual queremos obter o fator de balanceamento.

        Retorno:
        - int: O fator de balanceamento (altura da subárvore esquerda menos a altura da subárvore direita).
        """
        if not node:
            return 0
        return self.obter_altura(node.esquerda) - self.obter_altura(node.direita)

    def rotacao_direita(self, y):
        """
        Realiza uma rotação à direita em um nó para balancear a árvore.

        Parâmetros:
        - y (Node): O nó desbalanceado onde a rotação à direita será aplicada.

        Retorno:
        - Node: O novo nó raiz após a rotação.
        """
        x = y.esquerda
        T2 = x.direita
        x.direita = y
        y.esquerda = T2
        y.altura = 1 + max(self.obter_altura(y.esquerda), self.obter_altura(y.direita))
        x.altura = 1 + max(self.obter_altura(x.esquerda), self.obter_altura(x.direita))
        return x

    def rotacao_esquerda(self, x):
        """
        Realiza uma rotação à esquerda em um nó para balancear a árvore.

        Parâmetros:
        - x (Node): O nó desbalanceado onde a rotação à esquerda será aplicada.

        Retorno:
        - Node: O novo nó raiz após a rotação.
        """
        y = x.direita
        T2 = y.esquerda
        y.esquerda = x
        x.direita = T2
        x.altura = 1 + max(self.obter_altura(x.esquerda), self.obter_altura(x.direita))
        y.altura = 1 + max(self.obter_altura(y.esquerda), self.obter_altura(y.direita))
        return y

    def inserir(self, node, chave, valor):
        """
        Insere um novo nó na árvore AVL de forma recursiva e balanceada.

        Parâmetros:
        - node (Node): O nó atual durante a recursão.
        - chave (qualquer tipo comparável): A chave do novo nó.
        - valor (qualquer tipo): O valor associado à chave.

        Retorno:
        - Node: O nó atualizado após a inserção e o possível balanceamento.
        """
        if not node:
            return Node(chave, valor)
        if chave < node.chave:
            node.esquerda = self.inserir(node.esquerda, chave, valor)
        elif chave > node.chave:
            node.direita = self.inserir(node.direita, chave, valor)
        else:
            return node  # Chaves duplicadas não são permitidas
        
        node.altura = 1 + max(self.obter_altura(node.esquerda), self.obter_altura(node.direita))
        
        balanceamento = self.obter_fator_balanceamento(node)

        if balanceamento > 1 and chave < node.esquerda.chave:
            return self.rotacao_direita(node)
        if balanceamento < -1 and chave > node.direita.chave:
            return self.rotacao_esquerda(node)
        if balanceamento > 1 and chave > node.esquerda.chave:
            node.esquerda = self.rotacao_esquerda(node.esquerda)
            return self.rotacao_direita(node)
        if balanceamento < -1 and chave < node.direita.chave:
            node.direita = self.rotacao_direita(node.direita)
            return self.rotacao_esquerda(node)
        
        return node

    def inserir_produto(self, chave, valor):
        """
        Insere um produto na árvore AVL utilizando a chave como critério de ordenação.

        Parâmetros:
        - chave (qualquer tipo comparável): A chave para o produto (ex: nome do produto).
        - valor (qualquer tipo): O valor associado ao produto (ex: os detalhes do produto).

        Retorno:
        - None
        """
        self.raiz = self.inserir(self.raiz, chave, valor)

    def menor_valor(self, node):
        """
        Encontra o nó com o menor valor em uma subárvore.

        Parâmetros:
        - node (Node): O nó raiz da subárvore.

        Retorno:
        - Node: O nó com o menor valor.
        """
        atual = node
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def remover(self, node, chave):
        """
        Remove um nó da árvore AVL de forma recursiva, mantendo o balanceamento.

        Parâmetros:
        - node (Node): O nó atual durante a recursão.
        - chave (qualquer tipo comparável): A chave do nó que será removido.

        Retorno:
        - Node: O nó atualizado após a remoção e o possível balanceamento.
        """
        if not node:
            return node
        if chave < node.chave:
            node.esquerda = self.remover(node.esquerda, chave)
        elif chave > node.chave:
            node.direita = self.remover(node.direita, chave)
        else:
            if node.esquerda is None:
                return node.direita
            elif node.direita is None:
                return node.esquerda
            temp = self.menor_valor(node.direita)
            node.chave = temp.chave
            node.valor = temp.valor
            node.direita = self.remover(node.direita, temp.chave)

        node.altura = 1 + max(self.obter_altura(node.esquerda), self.obter_altura(node.direita))

        balanceamento = self.obter_fator_balanceamento(node)

        if balanceamento > 1 and self.obter_fator_balanceamento(node.esquerda) >= 0:
            return self.rotacao_direita(node)
        if balanceamento < -1 and self.obter_fator_balanceamento(node.direita) <= 0:
            return self.rotacao_esquerda(node)
        if balanceamento > 1 and self.obter_fator_balanceamento(node.esquerda) < 0:
            node.esquerda = self.rotacao_esquerda(node.esquerda)
            return self.rotacao_direita(node)
        if balanceamento < -1 and self.obter_fator_balanceamento(node.direita) > 0:
            node.direita = self.rotacao_direita(node.direita)
            return self.rotacao_esquerda(node)

        return node

    def remover_produto(self, chave):
        """
        Remove um produto da árvore AVL com base na chave fornecida.

        Parâmetros:
        - chave (qualquer tipo comparável): A chave do produto que será removido.

        Retorno:
        - None
        """
        self.raiz = self.remover(self.raiz, chave)

    def buscar(self, node, chave):
        """
        Realiza uma busca recursiva na árvore AVL.

        Parâmetros:
        - node (Node): O nó atual durante a recursão.
        - chave (qualquer tipo comparável): A chave do nó que está sendo procurado.

        Retorno:
        - Node: O nó encontrado ou None se não for encontrado.
        """
        if not node or node.chave == chave:
            return node
        if chave < node.chave:
            return self.buscar(node.esquerda, chave)
        return self.buscar(node.direita, chave)

    def buscar_produto(self, chave):
        """
        Busca um produto na árvore AVL com base na chave fornecida.

        Parâmetros:
        - chave (qualquer tipo comparável): A chave do produto que está sendo buscado.

        Retorno:
        - Node: O nó encontrado ou None se não for encontrado.
        """
        return self.buscar(self.raiz, chave)


# Classe de Gerenciamento de Produtos com AVL integrada
class GerenciamentoProdutos:
    def __init__(self):
        """
        Inicializa a estrutura de gerenciamento de produtos.

        Atributos:
        - produtos_avl (AVLTree): Estrutura AVL para armazenar os produtos e permitir busca eficiente por nome.
        - produtos_hash (dict): Um dicionário que mapeia códigos de barras para produtos, permitindo busca eficiente por código de barras.
        - pilha_reabastecimento (list): Uma pilha para armazenar produtos a serem reabastecidos, implementada como uma lista.
        - fila_pedidos (list): Uma fila para armazenar pedidos de produtos, implementada como uma lista.
        """
        self.produtos_avl = AVLTree()  
        self.produtos_hash = {}  
        self.pilha_reabastecimento = []  
        self.fila_pedidos = []  

    def cadastrar_produto(self, produto):
        """
        Cadastra um produto no sistema de gerenciamento.

        Parâmetros:
        - produto (dict): Um dicionário contendo as informações do produto, como nome, categoria, preço, e código de barras.

        Ações:
        - Insere o produto na árvore AVL (para busca por nome).
        - Insere o produto na tabela hash (para busca por código de barras).
        """
        self.produtos_avl.inserir_produto(produto["nome"], produto)
        self.produtos_hash[produto["codigo_barras"]] = produto

    def buscar_por_nome(self, nome):
        """
        Busca um produto pelo nome usando a árvore AVL.

        Parâmetros:
        - nome (str): O nome do produto que se deseja buscar.

        Retorno:
        - dict: O dicionário com as informações do produto encontrado ou None se não for encontrado.
        """
        no_encontrado = self.produtos_avl.buscar_produto(nome)
        return no_encontrado.valor if no_encontrado else None

    def buscar_por_codigo_barras(self, codigo_barras):
        """
        Busca um produto pelo código de barras usando a tabela hash.

        Parâmetros:
        - codigo_barras (str): O código de barras do produto que se deseja buscar.

        Retorno:
        - dict: O dicionário com as informações do produto encontrado ou None se não for encontrado.
        """
        return self.produtos_hash.get(codigo_barras)

    def remover_produto(self, nome, codigo_barras):
        """
        Remove um produto do sistema, tanto da árvore AVL quanto da tabela hash.

        Parâmetros:
        - nome (str): O nome do produto que se deseja remover.
        - codigo_barras (str): O código de barras do produto que se deseja remover.

        Ações:
        - Remove o produto da árvore AVL (usando o nome).
        - Remove o produto da tabela hash (usando o código de barras).
        """
        self.produtos_avl.remover_produto(nome)
        self.produtos_hash.pop(codigo_barras, None)

    def listar_produtos(self, key="nome", reverse=False):
        """
        Lista os produtos ordenados por uma chave especificada.

        Parâmetros:
        - key (str): A chave pela qual os produtos devem ser ordenados (ex: "nome" ou "preco").
        - reverse (bool): Se True, ordena em ordem decrescente. Se False, ordem crescente (padrão).

        Retorno:
        - list: Uma lista de produtos ordenada de acordo com os critérios especificados.
        """
        produtos = list(self.produtos_hash.values())
        return self.quicksort(produtos, key, reverse)

    def quicksort(self, arr, key, reverse=False):
        """
        Implementa o algoritmo QuickSort para ordenar a lista de produtos.

        Parâmetros:
        - arr (list): A lista de produtos a ser ordenada.
        - key (str): A chave pela qual os produtos devem ser ordenados.
        - reverse (bool): Se True, ordena em ordem decrescente. Se False, ordem crescente (padrão).

        Retorno:
        - list: A lista de produtos ordenada.
        """
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x[key] < pivot[key]] if not reverse else [x for x in arr if x[key] > pivot[key]]
        middle = [x for x in arr if x[key] == pivot[key]]
        right = [x for x in arr if x[key] > pivot[key]] if not reverse else [x for x in arr if x[key] < pivot[key]]
        return self.quicksort(left, key, reverse) + middle + self.quicksort(right, key, reverse)

    def reabastecer(self, produto):
        """
        Adiciona um produto à pilha de reabastecimento.

        Parâmetros:
        - produto (dict): Um dicionário contendo as informações do produto a ser reabastecido.

        Ações:
        - Insere o produto no topo da pilha de reabastecimento.
        """
        self.pilha_reabastecimento.append(produto)

    def vender_produto(self):
        """
        Vende o último produto que foi reabastecido (usando a estrutura de pilha).

        Retorno:
        - dict: O dicionário com as informações do produto vendido ou None se a pilha estiver vazia.
        """
        if self.pilha_reabastecimento:
            return self.pilha_reabastecimento.pop()
        return None

    def adicionar_pedido(self, produto):
        """
        Adiciona um pedido à fila de pedidos.

        Parâmetros:
        - produto (dict): Um dicionário contendo as informações do produto que está sendo solicitado.

        Ações:
        - Insere o produto no final da fila de pedidos.
        """
        self.fila_pedidos.append(produto)

    def atender_pedido(self):
        """
        Atende o primeiro pedido da fila de pedidos (usando estrutura de fila).

        Retorno:
        - dict: O dicionário com as informações do pedido atendido ou None se a fila estiver vazia.
        """
        if self.fila_pedidos:
            return self.fila_pedidos.pop(0)
        return None

    def gerar_relatorio(self):
        """
        Gera um relatório com o total de produtos cadastrados e o valor total do estoque.

        Ações:
        - Calcula e imprime o número total de produtos e o valor total do estoque.
        - Imprime os detalhes de cada produto (nome, categoria, preço e código de barras).
        """
        total_produtos = len(self.produtos_hash)
        valor_total_estoque = sum([produto['preco'] for produto in self.produtos_hash.values()])
        print("Relatório de Produtos:")
        print(f"Total de produtos: {total_produtos}")
        print(f"Valor total do estoque: R$ {valor_total_estoque}")
        for produto in self.produtos_hash.values():
            print(f"Nome: {produto['nome']}, Categoria: {produto['categoria']}, Preço: {produto['preco']}, Código de Barras: {produto['codigo_barras']}")



# Criação da instância de GerenciamentoProdutos
gerente = GerenciamentoProdutos()

# Lista de produtos de exemplo
produtos_exemplo = [
    {"nome": "Smartphone XYZ", "categoria": "Smartphone", "preco": 1200.00, "codigo_barras": "1234567890123"},
    {"nome": "Laptop ABC", "categoria": "Laptop", "preco": 2500.00, "codigo_barras": "2345678901234"},
    {"nome": "Tablet QRS", "categoria": "Tablet", "preco": 800.00, "codigo_barras": "3456789012345"},
    {"nome": "Smartwatch LMN", "categoria": "Smartwatch", "preco": 400.00, "codigo_barras": "4567890123456"},
    {"nome": "Fone de Ouvido DEF", "categoria": "Acessórios", "preco": 150.00, "codigo_barras": "5678901234567"}
]

# Cadastrar produtos
for produto in produtos_exemplo:
    gerente.cadastrar_produto(produto)

# Buscar produto por nome
produto_buscado = gerente.buscar_por_nome("Laptop ABC")
print(f"Produto buscado por nome: {produto_buscado}")

# Buscar produto por código de barras
produto_buscado_codigo = gerente.buscar_por_codigo_barras("1234567890123")
print(f"Produto buscado por código de barras: {produto_buscado_codigo}")

# Listar produtos ordenados por nome (crescente)
produtos_ordenados_nome = gerente.listar_produtos(key="nome", reverse=False)
print("Produtos ordenados por nome (crescente):")
for produto in produtos_ordenados_nome:
    print(produto)

# Listar produtos ordenados por preço (decrescente)
produtos_ordenados_preco = gerente.listar_produtos(key="preco", reverse=True)
print("Produtos ordenados por preço (decrescente):")
for produto in produtos_ordenados_preco:
    print(produto)

# Reabastecer produtos
gerente.reabastecer({"nome": "Smartphone XYZ", "categoria": "Smartphone", "preco": 1200.00, "codigo_barras": "1234567890123"})
gerente.reabastecer({"nome": "Laptop ABC", "categoria": "Laptop", "preco": 2500.00, "codigo_barras": "2345678901234"})

# Vender o último produto reabastecido
produto_vendido = gerente.vender_produto()
print(f"Produto vendido (último reabastecido): {produto_vendido}")

# Adicionar pedidos
gerente.adicionar_pedido({"nome": "Tablet QRS", "categoria": "Tablet", "preco": 800.00, "codigo_barras": "3456789012345"})
gerente.adicionar_pedido({"nome": "Smartwatch LMN", "categoria": "Smartwatch", "preco": 400.00, "codigo_barras": "4567890123456"})

# Atender o primeiro pedido
pedido_atendido = gerente.atender_pedido()
print(f"Pedido atendido (primeiro da fila): {pedido_atendido}")

# Gerar relatório de produtos
gerente.gerar_relatorio()

