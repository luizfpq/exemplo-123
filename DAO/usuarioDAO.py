from database import db

class Usuario:
    #consulta pelo id
    @staticmethod
    def get_id(id): # função que busca no db o id da usuario
        return Usuario.query.get(id)
    #create
    @staticmethod
    def addUsuário(nome, email,senha): #função q adiciona uma usuario no db
        usuario = Usuario(nome = nome, email = email, senha = senha) #possivel validação, para melhorar se ja existe uma usuario com esse nome
        db.session.add(usuario)  #linha 9: usuario ta recebendo um novo objeto criado da classe usuario
        db.session.commit() #nn se esqueça do commit
        return usuario
    
    #read
    @staticmethod
    def getUsuario(nome,email): #pega o nome e email da usuario
        if email:
            return Usuario.query.filter_by(nome=nome, email=email).all() #consulta no db, filtrando pelo id
        return email

    #update
    @staticmethod #função estatica, ja q esta se relacionando com o db
    def atualizarUsuário(id,nome): #recebe como parametro o id e nome 
        usuario = Usuario.get_id(id) #pegando o id no db q foi passado
        if usuario :
            usuario.nome = nome #se a usuario existir, na tabela usuario, de id tal, o nome é modificado
            db.session.commit()
            return usuario
    
    #delete
    @staticmethod
    def deletarUsuário(id):
        usuario = Usuario.get_id(id)
        if usuario:
            db.session.delete(usuario) #mesma coisa do atualizar
            db.session.commit()
            return usuario