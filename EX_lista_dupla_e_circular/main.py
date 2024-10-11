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
            # Caso a lista esteja vazia
            self.head = novaMusica
            if self.circular:
                self.head.proximo = self.head
                if self.duplamente_encadeada:
                    self.head.anterior = self.head
        else:
            # Se já existe um head, colocamos novaMusica no começo
            novaMusica.proximo = self.head
            
            if self.duplamente_encadeada:
                novaMusica.anterior = None
                self.head.anterior = novaMusica
            
            # Atualizando head
            self.head = novaMusica

            # Se for circular, precisamos atualizar o último nó para apontar para o novo head
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
        anterior = None
        while atual.proximo != (self.head if self.circular else None):
            anterior = atual
            atual = atual.proximo
        if self.duplamente_encadeada and anterior:
            anterior.proximo = None
        if self.circular and anterior:
            anterior.proximo = self.head
            if self.duplamente_encadeada:
                self.head.anterior = anterior
        del atual

    def adicinarMusicaNaPosicao(self, nome, tempo, banda, posicao):
        novaMusica = Musica(nome, tempo, banda)
        
        if posicao == 0 or not self.head:
            # Se a posição for 0 ou a lista estiver vazia, adicionar no começo
            self.adicinarMusicaNoComeco(nome, tempo, banda)
            return

        atual = self.head
        indice = 0

        # Percorre a lista até encontrar a posição desejada ou o final da lista
        while indice < posicao - 1 and atual.proximo != (self.head if self.circular else None):
            atual = atual.proximo
            indice += 1

        # Se a posição desejada está além do tamanho atual da lista
        if indice != posicao - 1:
            print("Posição inválida")
            return

        # Ajustando os ponteiros
        novaMusica.proximo = atual.proximo
        atual.proximo = novaMusica

        if self.duplamente_encadeada:
            novaMusica.anterior = atual
            if novaMusica.proximo:
                novaMusica.proximo.anterior = novaMusica

        # Se for uma lista circular e o último nó precisa apontar para o head
        if self.circular and novaMusica.proximo == self.head:
            novaMusica.proximo = self.head
            if self.duplamente_encadeada:
                self.head.anterior = novaMusica
        
    def removerMusicaNaPosicao(self, posicao):
        if not self.head:
            print("Lista vazia")
            return
        
        if posicao == 0:
            # Se a posição for 0, remover a música do começo
            self.removerMusicaDoComeco()
            return

        atual = self.head
        indice = 0

        # Percorre a lista até o nó anterior ao que será removido
        while indice < posicao - 1 and atual.proximo != (self.head if self.circular else None):
            atual = atual.proximo
            indice += 1

        # Se a posição está fora dos limites da lista
        if indice != posicao - 1 or atual.proximo == (self.head if self.circular else None):
            print("Posição inválida")
            return

        removerMusica = atual.proximo

        # Atualiza o ponteiro 'proximo' para pular o nó removido
        atual.proximo = removerMusica.proximo

        if self.duplamente_encadeada:
            # Se for duplamente encadeada, ajustar o ponteiro 'anterior'
            if removerMusica.proximo:
                removerMusica.proximo.anterior = atual

        # Se for uma lista circular, ajustar o último nó para apontar para o head
        if self.circular and removerMusica.proximo == self.head:
            atual.proximo = self.head
            if self.duplamente_encadeada:
                self.head.anterior = atual

        del removerMusica


    def mover(self, posicao_origem, posicao_destino):
        if not self.head:
            print("Lista vazia")
            return
        
        if posicao_origem == posicao_destino:
            print("A posição de origem é igual à posição de destino. Nada a mover.")
            return
        
        # Encontre a música na posição de origem para recolher suas informações
        atual = self.head
        indice = 0
        
        # Percorre até a posição de origem
        while indice < posicao_origem and atual.proximo != (self.head if self.circular else None):
            atual = atual.proximo
            indice += 1

        # Se não encontrou a posição de origem
        if indice != posicao_origem:
            print("Posição de origem inválida")
            return
        
        # Guardar informações da música que será movida
        musica_nome = atual.nome
        musica_tempo = atual.tempo
        musica_banda = atual.banda

        # Remover a música da posição de origem
        self.removerMusicaNaPosicao(posicao_origem)
        
        # Adicionar a música na posição de destino
        self.adicinarMusicaNaPosicao(musica_nome, musica_tempo, musica_banda, posicao_destino)

        print(f"Música '{musica_nome}' movida de {posicao_origem} para {posicao_destino}")




#exmplo de uso 

# Criar uma playlist circular e duplamente encadeada
playlist = PlyList(duplamente_encadeada=True, circular=True)

# Adicionar músicas à playlist
playlist.adicinarMusicaNoComeco("Música A", "3:30", "Banda X")
playlist.adicinarMusicaFinal("Música B", "4:00", "Banda Y")
playlist.adicinarMusicaFinal("Música C", "2:45", "Banda Z")
playlist.adicinarMusicaFinal("Música D", "5:10", "Banda W")

# Exibir a playlist inicial
print("Playlist inicial:")
atual = playlist.head
contador = 0
while contador < 4: 
    print(f"{atual.nome} - {atual.banda} ({atual.tempo})")
    atual = atual.proximo
    contador += 1

# Mover música da posição 2 (Música C) para a posição 1 (após Música A)
playlist.mover(2, 1)

# Exibir a playlist após mover
print("\nPlaylist após mover:")
atual = playlist.head
contador = 0
while contador < 4:  
    print(f"{atual.nome} - {atual.banda} ({atual.tempo})")
    atual = atual.proximo
    contador += 1

# Remover a música da posição 1
playlist.removerMusicaNaPosicao(1)

# Exibir a playlist após a remoção
print("\nPlaylist após remover da posição 1:")
atual = playlist.head
contador = 0
while contador < 3: 
    print(f"{atual.nome} - {atual.banda} ({atual.tempo})")
    atual = atual.proximo
    contador += 1

