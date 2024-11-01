
from flask import Blueprint, render_template, request, redirect, url_for, session, abort, flash, make_response
from models import filmes, sessoes, Usuario

koga = Blueprint('koga', __name__)

@koga.route('/login', methods=['GET', 'POST']) 
def login():
    if request.method == 'GET':
        if sessoes.existe('nome'):
            return redirect(url_for('index'))
        return render_template('login.html')
    
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']

        usuario = next((u for u in filmes.USUARIOS if nome == u.nome and senha == u.senha), None)
        if usuario:
            sessoes.atualizar_login('nome', nome)
            sessoes.atualizar_login('tipo', usuario.tipo)
            return redirect(url_for('index'))

        flash('Credenciais incorretas.', 'warning')
        return redirect(url_for('koga.login'))

@koga.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        senha = request.form.get('senha')
        tipo = request.form.get('tipo', 'user')

        if any(usuario.nome == nome for usuario in filmes.USUARIOS):
            return render_template('registro.html', erro='Usuário já existe.')

        novo_usuario = Usuario(id=len(filmes.USUARIOS) + 1, nome=nome, senha=senha, tipo=tipo)
        filmes.USUARIOS.append(novo_usuario)

        return redirect(url_for('koga.login'))

    return render_template('registro.html')

@koga.route('/admin')
def admin():
    if sessoes.get('tipo') != 'admin':
        abort(401)
    return render_template('admin.html')

@koga.route('/carrinho')
def carrinho():
    carrinho = []
    for f in filmes.FILMES:
        quantidade = request.cookies.get(f'produto_{f.id}')
        if quantidade:
            carrinho.append({
                'nome': f.titulo,
                'quantidade': int(quantidade),
                'total': int(quantidade) * f.preco
            })
    return render_template('index.html', carrinho=carrinho)

@koga.route('/carrinho/add')
def add():
    id = request.args.get('id')
    resp = make_response(redirect(url_for('index')))
    cookie = request.cookies.get(f'produto_{id}')
    if cookie:
        resp.set_cookie(f'produto_{id}', str(int(cookie) + 1))
    else:
        resp.set_cookie(f'produto_{id}', "1")
    return resp

@koga.route('/carrinho/del')
def delete():
    id = request.args.get('id')
    resp = make_response(redirect(url_for('index')))
    cookie = request.cookies.get(f'produto_{id}')
    if cookie:
        if int(cookie) - 1 > 0:
            resp.set_cookie(f'produto_{id}', str(int(cookie) - 1))
        else:
            resp.set_cookie(f'produto_{id}', '', expires=0)
    else:
        flash('O produto não está no carrinho para ser removido.', 'warning')
    return resp

@koga.route('/logout')
def logout():
    sessoes.limpar_login()
    return redirect(url_for('koga.login'))

