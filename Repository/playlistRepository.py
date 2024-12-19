from DAO.playlistDAO import PlaylistDAO

class playlistRepository:
    def __init__(self) -> None:
        self.playlist = PlaylistDAO()

    def get_id(self,id):
        return self.playlist.get_id(id)

    def addPlaylist(self,nome):
        return self.playlist.addPlaylist(nome)
    
    def getPlaylist(self,id):
        return self.playlist.getPlaylist(id)

    def atualizarPlaylist(self,id,nome):
        return self.playlist.atualizarPlaylist(id,nome)

    def deletarPlaylist(self,id):
        return self.playlist.deletarPlaylist(id)