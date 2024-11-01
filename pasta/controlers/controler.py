from flask import Blueprint, render_template, request, redirect, url_for, session, abort, flash, make_response
from models import filmes, sessoes


koga = Blueprint('koga', __name__)

@koga.route('/login', methods=['GET', 'POST']) 
def login():
    if request.method == 'GET':
        if sessoes.existe('nome'):
            if sessoes.get('tipo') == 'admin':
                return redirect(url_for('koga.admin'))
            return redirect(url_for('index')) 
        return render_template('login.html')
    
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']

        usuario = next((u for u in filmes.USUARIOS if nome == u.nome and senha == u.senha), None)
        if usuario:
            sessoes.atualizar_login('nome', nome)
            sessoes.atualizar_login('tipo', usuario.tipo)

            
            if usuario.tipo == 'admin':
                return redirect(url_for('koga.admin'))
            else:
                return redirect(url_for('index')) 

        flash('Credenciais incorretas.', 'warning')
        return redirect(url_for('koga.login'))

@koga.route('/admin')
def admin():
    if sessoes.get('tipo') != 'admin':
        abort(401)
    return render_template('admin.html')

@koga.route('/carrinho/add')
def add():
    id = request.args.get('id')
    nome_usuario = sessoes.get('nome')
    resp = make_response()

    cookie = request.cookies.get(f'produto_{id}')
    if cookie:
        resp.set_cookie(f'produto_{id}', str(int(cookie) + 1), path='/')
    else:
        resp.set_cookie(f'produto_{id}', "1", path='/')

    carrinho = []
    for f in filmes.FILMES:
        quantidade = request.cookies.get(f'produto_{f.id}')
        if quantidade:
            carrinho.append({
                'titulo': f.titulo,
                'quantidade': int(quantidade),
                'total': int(quantidade) * f.preco
            })


    resp.set_data(render_template('index.html', c=carrinho, nome=nome_usuario, filmes=filmes.FILMES))
    return resp

@koga.route('/carrinho/del')
def delete():
    id = request.args.get('id')
    nome_usuario = sessoes.get('nome')
    resp = make_response()

    # Atualiza ou remove o cookie do produto
    cookie = request.cookies.get(f'produto_{id}')
    if cookie:
        if int(cookie) - 1 > 0:
            resp.set_cookie(f'produto_{id}', str(int(cookie) - 1), path='/')
        else:
            resp.set_cookie(f'produto_{id}', '', expires=0, path='/')
    else:
        flash('O produto não está no carrinho para ser removido.', 'warning')

    carrinho = []
    for f in filmes.FILMES:
        quantidade = request.cookies.get(f'produto_{f.id}')
        if quantidade:
            carrinho.append({
                'titulo': f.titulo,
                'quantidade': int(quantidade),
                'total': int(quantidade) * f.preco
            })


    resp.set_data(render_template('index.html', c=carrinho, nome=nome_usuario, filmes=filmes.FILMES))
    return resp

@koga.route('/logout')
def logout():
    sessoes.limpar_login()
    return redirect(url_for('koga.login'))

