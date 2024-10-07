from lista_duplamemte_encadiada import DoublyLinkedList

class Queue:
    def __init__(self) -> None:
        self.__lista = DoublyLinkedList()
    
    def enqueue(self, data):
        self.__lista.append(data)
    
    def is_empty(self):
        return self.__lista.size() == 0
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("A fila está vazia")
        
        front = self.__lista.head.data
        self.__lista.remove_at(0)
        return front
    
    def peek(self):
        if self.is_empty():
            raise IndexError("A fila está vazia")
        return self.__lista.head.data
    
    def print_queue(self):
        self.__lista.print_forward()
