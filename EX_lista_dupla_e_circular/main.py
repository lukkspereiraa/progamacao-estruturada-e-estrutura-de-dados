class Musica:
    def __init__(self,nome, tempo, banda) -> None:
        """Classe de musica represnetado um no da lista, como é uma lista esperace quendo adicinado algo, ter um ponteiro para o proximo e se possivel para o anterior
        Args:
            nome (String): o nome da musica adicinada
            tempo (String): o tempo da musica em minutos
            banda (String): nome da banda ou artista
        """

        self.nome = nome
        self.tempo = tempo
        self.banda = banda
        self.proximo = None
        self.anterior = None

class PlyList:
    def __init__(self, duplamente_encadeada=True) -> None:
        self.head = None 
        self.duplamente_encadeada = duplamente_encadeada 

    def listaDuplamenteEncadeada(self, valor):
        """Define se a lista será duplamente ou simplesmente encadeada."""
        self.duplamente_encadeada = valor

    def adicinarMusicaNoComeco(self, nome, tempo, banda):
        novaMusica = Musica(nome, tempo, banda)
        if not self.head:
            self.head = novaMusica
        else:
            novaMusica.proximo = self.head
            if self.duplamente_encadeada:
                self.head.anterior = novaMusica
            self.head = novaMusica

    def removerMusicaDoComeco(self):
        if self.head is None:
            print("Lista vazia")
            return
        removerMusica = self.head
        self.head = self.head.proximo
        if self.duplamente_encadeada and self.head:
            self.head.anterior = None
        del removerMusica

    def adicinarMusicaFinal(self, nome, tempo, banda):
        novaMusica = Musica(nome, tempo, banda)

        if not self.head:
            self.head = novaMusica
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novaMusica
            if self.duplamente_encadeada:
                novaMusica.anterior = atual

    def removerMusicaDoFinal(self):
        if self.head is None:
            print("Lista vazia")
            return
        
        if self.head.proximo is None:
            removerMusica = self.head
            self.head = None
            del removerMusica
            return
        
        atual = self.head
        while atual.proximo:
            atual = atual.proximo
        if self.duplamente_encadeada:
            atual.anterior.proximo = None
        else:
            anterior = self.head
            while anterior.proximo != atual:
                anterior = anterior.proximo
            anterior.proximo = None
        del atual

    def adicinarMusicaNaPosicao(self, nome, tempo, banda, posicao):
        novaMusica = Musica(nome, tempo, banda)
        if posicao == 0 or not self.head:
            self.adicinarMusicaNoComeco(nome, tempo, banda)
            return
        atual = self.head
        indice = 0

        while atual.proximo and indice < posicao - 1:
            atual = atual.proximo
            indice += 1
        novaMusica.proximo = atual.proximo

        if self.duplamente_encadeada:
            novaMusica.anterior = atual
            if atual.proximo:
                atual.proximo.anterior = novaMusica
        atual.proximo = novaMusica

    def removerMusicaNaPosicao(self, posicao):
        if self.head is None:
            print("Lista vazia")
            return
        
        if posicao == 0:
            self.removerMusicaDoComeco()
            return
        atual = self.head
        indice = 0

        while atual.proximo and indice < posicao:
            atual = atual.proximo
            indice += 1

        if indice != posicao:
            print("Posição inválida")
            return
        
        if self.duplamente_encadeada:
            if atual.anterior:
                atual.anterior.proximo = atual.proximo
            if atual.proximo:
                atual.proximo.anterior = atual.anterior
        else:
            anterior = self.head
            while anterior.proximo != atual:
                anterior = anterior.proximo
            anterior.proximo = atual.proximo
        del atual


#exmplo de uso 

# Criar uma lista duplamente encadeada
playlist = PlyList()
playlist.listaDuplamenteEncadeada(True)

# Adicionar músicas
playlist.adicinarMusicaNoComeco("Música A", "3:30", "Banda X")
playlist.adicinarMusicaFinal("Música B", "4:00", "Banda Y")
playlist.adicinarMusicaNaPosicao("Música C", "2:45", "Banda Z", 1)

# Remover músicas
playlist.removerMusicaDoFinal()

# Agora, mudar para uma lista simplesmente encadeada
playlist.listaDuplamenteEncadeada(False)

# Adicionar e remover músicas usando lista simplesmente encadeada
playlist.adicinarMusicaNoComeco("Música D", "3:15", "Banda W")
playlist.removerMusicaDoFinal()
