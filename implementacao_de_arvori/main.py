class AVLTree:
    class Node:
        def __init__(self, value):
            '''
            Inicializa um nó da árvore AVL.
            
            :param value: Valor do nó.
            '''
            self.value = value
            self.left = None
            self.right = None
            self.height = 1

    def __init__(self):
        '''
        Inicializa a árvore AVL.
        '''
        self.root = None

    def get_height(self, node):
        '''
        Obtém a altura de um nó.
        
        :param node: Nó atual.
        :return: Altura do nó.
        '''
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        '''
        Calcula o fator de balanceamento de um nó.
        
        :param node: Nó atual.
        :return: Fator de balanceamento.
        '''
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, y):
        '''
        Realiza a rotação à direita no nó y.
        
        :param y: Nó atual.
        :return: Novo nó raiz após a rotação.
        '''
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def rotate_left(self, x):
        '''
        Realiza a rotação à esquerda no nó x.
        
        :param x: Nó atual.
        :return: Novo nó raiz após a rotação.
        '''
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def rotate_left_right(self, node):
        '''
        Realiza a rotação dupla esquerda-direita.
        
        :param node: Nó atual.
        :return: Novo nó raiz após a rotação.
        '''
        node.left = self.rotate_left(node.left)
        return self.rotate_right(node)

    def rotate_right_left(self, node):
        '''
        Realiza a rotação dupla direita-esquerda.
        
        :param node: Nó atual.
        :return: Novo nó raiz após a rotação.
        '''
        node.right = self.rotate_right(node.right)
        return self.rotate_left(node)

    def insert(self, root, value):
        '''
        Insere um novo nó na árvore AVL e balanceia a árvore se necessário.
        
        :param root: Raiz atual da árvore.
        :param value: Valor a ser inserido.
        :return: Nova raiz após a inserção e balanceamento.
        '''
        if not root:
            return self.Node(value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and value < root.left.value:
            return self.rotate_right(root)

        if balance < -1 and value > root.right.value:
            return self.rotate_left(root)

        if balance > 1 and value > root.left.value:
            return self.rotate_left_right(root)

        if balance < -1 and value < root.right.value:
            return self.rotate_right_left(root)

        return root

    def insert_value(self, value):
        '''
        Método público para inserir um valor na árvore AVL.
        
        :param value: Valor a ser inserido.
        '''
        self.root = self.insert(self.root, value)

    def get_min_value_node(self, root):
        '''
        Encontra o nó com o menor valor em uma subárvore.
        
        :param root: Raiz da subárvore.
        :return: Nó com o menor valor.
        '''
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)

    def delete(self, root, value):
        '''
        Remove um nó da árvore AVL e a balanceia se necessário.
        
        :param root: Raiz atual da árvore.
        :param value: Valor a ser removido.
        :return: Nova raiz após a remoção e balanceamento.
        '''
        if not root:
            return root
        elif value < root.value:
            root.left = self.delete(root.left, value)
        elif value > root.value:
            root.right = self.delete(root.right, value)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self.get_min_value_node(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)

        if root is None:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.rotate_right(root)

        if balance > 1 and self.get_balance(root.left) < 0:
            return self.rotate_left_right(root)

        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.rotate_left(root)

        if balance < -1 and self.get_balance(root.right) > 0:
            return self.rotate_right_left(root)

        return root

    def delete_value(self, value):
        '''
        Método público para remover um valor da árvore AVL.
        
        :param value: Valor a ser removido.
        '''
        self.root = self.delete(self.root, value)

    def in_order(self, root):
        '''
        Realiza o percurso em ordem (in-order).
        
        :param root: Raiz da árvore.
        :return: Lista de valores em ordem.
        '''
        result = []
        if root:
            result = self.in_order(root.left)
            result.append(root.value)
            result = result + self.in_order(root.right)
        return result

    def pre_order(self, root):
        '''
        Realiza o percurso pré-ordem (pre-order).
        
        :param root: Raiz da árvore.
        :return: Lista de valores em pré-ordem.
        '''
        result = []
        if root:
            result.append(root.value)
            result = result + self.pre_order(root.left)
            result = result + self.pre_order(root.right)
        return result

    def post_order(self, root):
        '''
        Realiza o percurso pós-ordem (post-order).
        
        :param root: Raiz da árvore.
        :return: Lista de valores em pós-ordem.
        '''
        result = []
        if root:
            result = self.post_order(root.left)
            result = result + self.post_order(root.right)
            result.append(root.value)
        return result

if __name__ == "__main__":
    avl_tree = AVLTree()

    values = [10, 20, 30, 40, 50, 25]
    for val in values:
        avl_tree.insert_value(val)

    print("Percurso em ordem: ", avl_tree.in_order(avl_tree.root))
    print("Percurso pré-ordem: ", avl_tree.pre_order(avl_tree.root))
    print("Percurso pós-ordem: ", avl_tree.post_order(avl_tree.root))

    avl_tree.delete_value(40)
    print("Percurso em ordem após remoção de 40: ", avl_tree.in_order(avl_tree.root))
