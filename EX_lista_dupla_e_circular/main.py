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
    def __init__(self) -> None:
            self.herd = None

    def adicinarMusicaNoComeco(self, nome, tempo, banda):
        novaMusica = Musica(nome, tempo, banda)
        if  not self.herd:
              self.herd = novaMusica
        else:
            novaMusica.proximo =  self.herd  
            self.herd.anterior = novaMusica
            self.herd = novaMusica
    
    def removerMusicaDocomeco(self):
        if self.herd is None:
            print("Lista vazia")
            return
        

        if self.herd:
            self.herd.anterior = None

        removerMusica = self.herd
        self.herd = self.herd.proximo

        del removerMusica

    def adicinarMusicaFinal(self, nome, tempo, banda):
        novaMusica = Musica(nome, tempo, banda)
        if not self.herd:
            self.herd = novaMusica
        else:
            atual = self.herd
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novaMusica 
            novaMusica.anterior = atual  
   
        
# Exemplo de uso:
playlist = PlyList()
playlist.adicinarMusicaNoComeco("Música A", "3:30", "Banda X")
playlist.adicinarMusicaFinal("Música B", "4:00", "Banda Y")
playlist.adicinarMusicaFinal("Música C", "2:45", "Banda Z")
            