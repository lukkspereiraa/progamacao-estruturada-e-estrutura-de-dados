class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node


    def remove_at_beginning(self):
        if self.head is None:
            print("A lista está vazia.")
            return      
        
        removed_node = self.head
        
        self.head = self.head.next
        
        if self.head is not None:
            self.head.prev = None
            
        del removed_node 

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def display_backward(self):
        current = self.head
        if not current:
            return
        while current.next:
            current = current.next
        while current:
            print(current.data, end=' ')
            current = current.prev
        print()


dll = DoublyLinkedList()
dll.insert_at_beginning(3)
dll.insert_at_beginning(2)
dll.insert_at_beginning(1)

print("Lista (para frente):")
dll.display_forward()

dll.remove_at_beginning()
print("Lista após remover o primeiro elemento (para frente):")
dll.display_forward()

dll.remove_at_beginning()
print("Lista após remover mais um elemento (para frente):")
dll.display_forward()