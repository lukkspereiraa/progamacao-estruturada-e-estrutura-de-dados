from node import Node

class DoublyLinkedList:
    def __init__(self):
        self.head = None  
        self.tail = None  

    # Método para inserir no final (append)
    def append(self, data):
        new_node = Node(data)
        if self.tail is None:  
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    # Método para inserir no início (prepend)
    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:  
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Método para inserir em uma posição específica (insert)
    def insert(self, index, data):
        if index == 0: 
            self.prepend(data)
            return
        new_node = Node(data)
        current = self.head
        for i in range(index - 1):
            if current is None:
                raise IndexError("Index out of bounds")
            current = current.next
        if current == self.tail:  
            self.append(data)
        else:
            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node

    # Método para remover um nó específico (remove)
    def remove(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                elif current == self.tail:
                    self.tail = current.prev
                    if self.tail:
                        self.tail.next = None
                else:  
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return
            current = current.next
        raise ValueError("Data not found in the list")

    # Método para remover pelo índice (remove_at)
    def remove_at(self, index):
        if self.head is None:
            raise IndexError("Remove from empty list")
        
        current = self.head
        for i in range(index):
            if current is None:
                raise IndexError("Index out of bounds")
            current = current.next

        if current == self.head:
            self.head = current.next
            if self.head:
                self.head.prev = None
        elif current == self.tail:
            self.tail = current.prev
            if self.tail:
                self.tail.next = None
        else:  
            current.prev.next = current.next
            current.next.prev = current.prev

    # Método para obter um elemento por índice (get)
    def get(self, index):
        current = self.head
        for i in range(index):
            if current is None:
                raise IndexError("Index out of bounds")
            current = current.next
        return current.data

    # Método para verificar se a lista contém um valor (contains)
    def contains(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    # Método para limpar a lista (clear)
    def clear(self):
        self.head = self.tail = None

    # Método para obter o tamanho da lista (size)
    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    # Método para exibir a lista do início ao fim (print_forward)
    def print_forward(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))

    # Método para exibir a lista do fim ao início (print_backward)
    def print_backward(self):
        elements = []
        current = self.tail
        while current:
            elements.append(str(current.data))
            current = current.prev
        print(" <- ".join(elements))