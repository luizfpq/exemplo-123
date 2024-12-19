from DAO.usuarioDAO import UsuarioDAO  # Acesso ao DAO de Usuario

class UsuarioRepository:
    def __init__(self) -> None:
        self.usuario_dao = UsuarioDAO()

    def get_id(self, id):
        return self.usuario_dao.get_id(id)

    def addUsuario(self, nome, email):
        return self.usuario_dao.addUsuario(nome, email)

    def getUsuario(self, nome, email):
        return self.usuario_dao.getUsuario(nome, email)

    def atualizarUsuario(self, id, nome):
        return self.usuario_dao.atualizarUsuario(id, nome)

    def deletarUsuario(self, id):
        return self.usuario_dao.deletarUsuario(id)
