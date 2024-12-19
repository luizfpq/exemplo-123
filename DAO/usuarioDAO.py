from Model.Usuario import Usuario  # Certifique-se de que o caminho está correto

class UsuarioDAO:
    @classmethod
    def get_id(cls, id):  # função que busca no db o id do usuário
        return Usuario.query.get(id)

    @classmethod
    def addUsuario(cls, nome, email):  # Função que adiciona um usuário no db
        usuario = Usuario(nome=nome, email=email)
        db.session.add(usuario)
        db.session.commit()
        return usuario

    @classmethod
    def getUsuario(cls, nome, email):  # Pega o nome e email do usuário
        if email:
            return Usuario.query.filter_by(nome=nome, email=email).first()
        return None

    @classmethod
    def atualizarUsuario(cls, id, nome):  # Recebe como parâmetro o id e nome
        usuario = cls.get_id(id)
        if usuario:
            usuario.nome = nome
            db.session.commit()
            return usuario

    @classmethod
    def deletarUsuario(cls, id):
        usuario = cls.get_id(id)
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
            return usuario
