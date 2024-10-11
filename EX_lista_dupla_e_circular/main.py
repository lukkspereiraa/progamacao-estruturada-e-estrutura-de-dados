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
    def __init__(self, duplamente_encadeada=True, circular=False) -> None:
        self.head = None
        self.duplamente_encadeada = duplamente_encadeada
        self.circular = circular

    def listaDuplamenteEncadeada(self, valor):
        """Define se a lista será duplamente ou simplesmente encadeada."""
        self.duplamente_encadeada = valor

    def listaCircular(self, valor):
        """Define se a lista será circular."""
        self.circular = valor

    def adicinarMusicaNoComeco(self, nome, tempo, banda):
        novaMusica = Musica(nome, tempo, banda)
        if not self.head:
            self.head = novaMusica
            if self.circular:
                self.head.proximo = self.head
                if self.duplamente_encadeada:
                    self.head.anterior = self.head
        else:
            novaMusica.proximo = self.head
            if self.duplamente_encadeada:
                novaMusica.anterior = None
                self.head.anterior = novaMusica
            self.head = novaMusica
            if self.circular:
                ultimo = self.head
                while ultimo.proximo != self.head.proximo:
                    ultimo = ultimo.proximo
                ultimo.proximo = self.head
                if self.duplamente_encadeada:
                    self.head.anterior = ultimo

    def removerMusicaDoComeco(self):
        if not self.head:
            print("Lista vazia")
            return
        if self.head == self.head.proximo:
            self.head = None
            return
        removerMusica = self.head
        self.head = self.head.proximo
        if self.duplamente_encadeada:
            self.head.anterior = None
        if self.circular:
            ultimo = self.head
            while ultimo.proximo != removerMusica:
                ultimo = ultimo.proximo
            ultimo.proximo = self.head
            if self.duplamente_encadeada:
                self.head.anterior = ultimo
        del removerMusica

    def adicinarMusicaFinal(self, nome, tempo, banda):
        novaMusica = Musica(nome, tempo, banda)
        if not self.head:
            self.head = novaMusica
            if self.circular:
                self.head.proximo = self.head
                if self.duplamente_encadeada:
                    self.head.anterior = self.head
        else:
            atual = self.head
            while atual.proximo != (self.head if self.circular else None):
                atual = atual.proximo
            atual.proximo = novaMusica
            if self.duplamente_encadeada:
                novaMusica.anterior = atual
            if self.circular:
                novaMusica.proximo = self.head
                if self.duplamente_encadeada:
                    self.head.anterior = novaMusica

    def removerMusicaDoFinal(self):
        if not self.head:
            print("Lista vazia")
            return
        if self.head.proximo == self.head:
            self.head = None
            return
        atual = self.head
        while atual.proximo != (self.head if self.circular else None):
            anterior = atual
            atual = atual.proximo
        if self.duplamente_encadeada:
            anterior.proximo = None
        if self.circular:
            anterior.proximo = self.head
            if self.duplamente_encadeada:
                self.head.anterior = anterior
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


# Ativando a funcionalidade de lista circular
playlist.listaCircular(True)

# Adicionar e remover músicas usando lista simplesmente encadeada
playlist.adicinarMusicaNoComeco("Música D", "3:15", "Banda W")
playlist.removerMusicaDoFinal()
