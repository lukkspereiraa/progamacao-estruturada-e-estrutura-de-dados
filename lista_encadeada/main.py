class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            
    def insert_no_comeco(self):
        while True:
            print()
        
     
    def display(self):
        current = self.head
        if not current:
            print('Lista vazia')
        else:
            while current:
                print(current.data,"->")
                current = current.next
            print("None")

list = LinkedList()
list.insert_at_beginning(10)
list.insert_at_beginning(1)
list.insert_at_beginning(20)
list.insert_at_beginning(4)

list.display()
