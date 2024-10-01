from lista_duplamemte_encadiada import DoublyLinkedList

class Stack:
    def __init__(self) -> None:
        self.__lista = DoublyLinkedList()
    
    def push(self, data):
        self.__lista.append(data)
    
    def is_empty(self):
        return self.__lista.size() == 0
    
    def pop(self):
        if self.is_empty():
            raise IndexError("A pilha esta vazia")
        
        top = self.__lista.tail.data
        self.__lista.remove_at(self.__lista.size() - 1)
        return top
    
    def peek(self):
        if self.is_empty():
            raise IndexError("A pilha esta vazia")
        return self.__lista.tail.data
    
    def print_stack(self):
        self.__lista.print_backward()

        
#testes
