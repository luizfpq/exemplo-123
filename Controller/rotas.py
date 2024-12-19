from flask import Blueprint, session, render_template, request, redirect, url_for, flash
import json
from datetime import datetime
from pathlib import Path
from database import db
from Model import Usuario
from Repository.usuarioRepository import UsuarioRepository

# Blueprint 
music = Blueprint('music', __name__)
usuario_repository = UsuarioRepository()  # Renomeado para seguir a convenção

#Caminho para o Json
log_path = Path("Model/log.json")

# página inicial:
@music.route('/')
def index():
    if 'nome' in session:
        nome_usuario = session.get('nome')
        return render_template('inicio.html', nome_usuario=nome_usuario)
    return render_template('inicio.html')

# rota da página de login
@music.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome = request.form['username']
        email = request.form['email']
        senha = request.form['password']
        
        #busca o nome e o email do usuario:
        usuario = usuario_repository.getUsuario(nome, email)

        # o usuario existir, então ele retorna a função playmusic
        if usuario and usuario.senha == senha:
            session['nome'] = usuario.nome
            if not log_path.exists() or log_path.stat().st_size == 0:
                data = [{
                    "nome": nome,
                    "email": email,
                    "timestamp": datetime.now().isoformat()
                }]
                with open(log_path, "w") as f:
                    json.dump(data, f, indent=4)
            else:
                with open(log_path, "r") as f:
                    try:
                        file_data = json.load(f)
                        if isinstance(file_data, dict):  # Handle the case where the JSON is a dict
                            file_data = [file_data]
                    except json.JSONDecodeError:
                        file_data = []

                new_entry = {
                    "nome": nome,
                    "email": email,
                    "timestamp": datetime.now().isoformat()
                }
                file_data.append(new_entry)

                with open(log_path, "w") as f:
                    json.dump(file_data, f, indent=4)
                    
            return redirect(url_for('music.playmusic'))
        
        #se o usuario não existir, ele adiciona ao banco de dados
        elif not usuario:
            novo_usuario = usuario_repository.addUsuario(nome, email, senha)
            session['nome'] = novo_usuario.nome

            # Adiciona ao log
            log = json.load(open(log_path, "r"))
            log[novo_usuario.email] = datetime.now().isoformat()
            json.dump(log, open(log_path, "w"), sort_keys=True, indent=4)
            
            return redirect(url_for('music.playmusic'))  

        # Caso de erro: usuário ou senha inválidos
        else:
            flash('Usuário ou senha inválidos!', 'error')
    return render_template('login.html')

#rota da playlist do usuário
@music.route('/MinhaPlaylist', methods=['GET', 'POST'])
def playmusic():
    return render_template('playlistUser.html')

#rota da playlist do usuário
@music.route('/logout')
def logout():
    # Melhoria: remoção segura da sessão
    session.pop('nome', None)  
    return redirect(url_for('music.index'))
    # render_template('inicio.html')
