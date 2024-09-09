class ListaLinear:
    def __init__(self):
        self.lista = []

    def append(self, elemento):
        self.lista = self.lista + [elemento]

    def insert(self, posicao, elemento):
        self.lista = self.lista[:posicao] + [elemento] + self.lista[posicao]

    def remove(self, elemento):
        nova_lsista = []
        encotrado = False
        for i in self.lista:
            if i == elemento and not encotrado:
                encotrado = True
            else:
                nova_lsista.append(i)
        self.lista = nova_lsista

